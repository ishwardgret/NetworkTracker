

import pyshark
import db

interface = 'en0'

def capturePackets(interface, time):
    """
    Params:
    interface : network interface name i.e. for mac 'en0'
    displayFilter: name to be filter 
    time: time for timeout
    """

    print("\nPacket  Capturing Started ")
    capture = pyshark.LiveCapture(interface=interface, display_filter='icmpv6')
    capture.sniff(timeout=time)

    return capture

def processPacket():
    """This is packet porcessing
    It process the packets which involves following:
    1. Parse the ICMP layers packets 
    2. Fetch ICMP type 
    3. find for neighbour solicitation 
    4. Insert  to db table 

    """
    # creating database 
    # db.createDB()
    # db.createTables()

    # Flushing database
    db.truncateTAbles()

    packets = capturePackets(interface, 60)
    print("Received Packets: ", packets)

    # looping on received packets 
    for packet in packets:
        icmpv6Type = packet.icmpv6.type
        # print("ICMP Type : ", icmpv6Type)

        if icmpv6Type == "135":
            # print(" Target Address ->   ", packet.icmpv6.nd_ns_target_address)
            targetAddress = packet.icmpv6.nd_ns_target_address
            # print(type(targetAddress))

            if str(targetAddress) != "fe80\:\:1":
                print("Target Address via NS->  ", targetAddress)

                fetchDuplication = db.fetchDataFromLLADB(targetAddress)

                # print(fetchDuplication)
                if not fetchDuplication:
                    db.insertDataInLLADB(targetAddress)
                else: 
                    dublicateAddress = db.fetchDataFromDADDB(targetAddress)
                    if not dublicateAddress:
                        db.insertDataInDADDB(targetAddress)
    
        
        elif icmpv6Type == "136":
            print("Link Local Address via NA -> ", packet.icmpv6.nd_na_target_address)
            neighbourAdAddress = packet.icmpv6.nd_na_target_address

            fetchAdAddress = db.fetchDataFromDADDB(neighbourAdAddress)
            # print(fetchAdAddress)
            if not fetchAdAddress:
                # check whether address is in LLADB 
                # attacker address never arrive in NS
                isAdInNs = db.fetchDataFromLLADB(neighbourAdAddress)
                if not isAdInNs:
                    print("*****************")
                    print("Attack Confirmed =====>", neighbourAdAddress)
                    print("*****************")
            else:
                print("*********************************")
                print("Duplication Address Detected")
                print("*********************************")



processPacket()
