"""
Copyright Ishwar Singh Bhandari 
(c) ishwaryb@gmail.com 2019
"""

import pyshark
import db
import argparse



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--interface", required=True,
	help="Name of network interface")
args = vars(ap.parse_args())

interface = args["interface"]

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
            print(" Target Address ->   ", packet.icmpv6.nd_ns_target_address)
            targetAddress = packet.icmpv6.nd_ns_target_address
            # print(type(targetAddress))

            if str(targetAddress) != "fe80\:\:1":
                # print(type(sourceLLA))
                print("Target Address ->  ", targetAddress)

                fetchDuplication = db.fetchDataFromLLADB(targetAddress)

                print(fetchDuplication)
                if not fetchDuplication:
                    db.insertDataInLLADB(targetAddress)
                else: 
                    db.insertDataInDADDB(targetAddress)
        
        elif icmpv6Type == "136":
            print("Neighbour Advertisement Address -> ", packet.icmpv6.nd_na_target_address)
            neighbourAdAddress = packet.icmpv6.nd_na_target_address

            fetchAdAddress = db.fetchDataFromDADDB(neighbourAdAddress)
            print(fetchAdAddress)
            if not fetchAdAddress:
                print("*****************")
                print("Attack Confirmed =====>", neighbourAdAddress)
                print("*****************")
            else:
                print("*********************************")
                print("Duplication Address Detected")
                print("*********************************")



processPacket()
