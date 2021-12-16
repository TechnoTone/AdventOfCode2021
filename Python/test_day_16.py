import day_16
from utils import Input

DATA = Input.day(16).raw()


def test_day_16_decode_value():
    packet = day_16.Packet.from_str("D2FE28")
    assert packet.version == 6
    assert packet.typeId == 4
    assert packet.value == 2021
    assert packet.packets == []


def test_day_16_decode_operator():
    packet = day_16.Packet.from_str("38006F45291200")
    assert packet.version == 1
    assert packet.typeId == 6
    assert packet.packets.__len__() == 2
    assert packet.packets[0].version == 6
    assert packet.packets[0].typeId == 4
    assert packet.packets[0].value == 10
    assert packet.packets[0].packets == []
    assert packet.packets[1].version == 2
    assert packet.packets[1].typeId == 4
    assert packet.packets[1].value == 20
    assert packet.packets[1].packets == []


def test_day_16_sum_packet_versions():
    assert day_16.part_1("8A004A801A8002F478") == 16
    assert day_16.part_1("620080001611562C8802118E34") == 12
    assert day_16.part_1("C0015000016115A2E0802F182340") == 23
    assert day_16.part_1("A0016C880162017C3686B18A3D4780") == 31


def test_day_16_part_1_solution():
    assert day_16.part_1(DATA) == 1014


def test_day_16_part_2_examples():
    assert day_16.part_2("C200B40A82") == 3
    assert day_16.part_2("04005AC33890") == 54
    assert day_16.part_2("880086C3E88112") == 7
    assert day_16.part_2("CE00C43D881120") == 9
    assert day_16.part_2("D8005AC2A8F0") == 1
    assert day_16.part_2("F600BC2D8F") == 0
    assert day_16.part_2("9C005AC2F8F0") == 0
    assert day_16.part_2("9C0141080250320F1802104A08") == 1


def test_day_16_part_2_solution():
    assert day_16.part_2(DATA) == 1922490999789
