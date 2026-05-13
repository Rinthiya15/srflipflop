import cocotb
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def sr_test(dut):

    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await Timer(10, units="ns")
    dut.rst_n.value = 1

    # HOLD
    dut.ui_in.value = 0b00
    await RisingEdge(dut.clk)

    # SET
    dut.ui_in.value = 0b01
    await RisingEdge(dut.clk)

    # RESET
    dut.ui_in.value = 0b10
    await RisingEdge(dut.clk)

    # INVALID
    dut.ui_in.value = 0b11
    await RisingEdge(dut.clk)

    await Timer(10, units="ns")
