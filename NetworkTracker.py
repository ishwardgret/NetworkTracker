"""
Copyright Ishwar Singh Bhandari 
(c) ishwaryb@gmail.com 2019
"""

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
        print("ICMP Type : ", icmpv6Type)

        if icmpv6Type == "135":
            print(" Target Address ->   ", packet.icmpv6.nd_ns_target_address)
            targetAddress = packet.icmpv6.nd_ns_target_address
            print(type(targetAddress))

            if str(targetAddress) != "fe80\:\:1":
                # print(type(sourceLLA))
                print("Target Address ->  ", targetAddress)

                fetchDuplication = db.fetchDataFromLLADB(targetAddress)

                print(fetchDuplication)
                if not fetchDuplication:
                    db.insertDataInLLADB(targetAddress)
                else: 
                    db.insertDataInDADDB(targetAddress)

processPacket()
