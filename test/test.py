import cocotb
from cocotb.triggers import RisingEdge, Timer


async def reset_dut(dut):
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    await Timer(10, units="ns")
    dut.rst_n.value = 1
    await Timer(10, units="ns")


@cocotb.test()
async def sr_flipflop_test(dut):

    # Reset
    await reset_dut(dut)

    # ----------------
    # HOLD (S=0 R=0)
    # ----------------
    dut.ui_in.value = 0b00
    await RisingEdge(dut.clk)

    # ----------------
    # SET (S=1 R=0)
    # ----------------
    dut.ui_in.value = 0b01
    await RisingEdge(dut.clk)

    # ----------------
    # HOLD
    # ----------------
    dut.ui_in.value = 0b00
    await RisingEdge(dut.clk)

    # ----------------
    # RESET (S=0 R=1)
    # ----------------
    dut.ui_in.value = 0b10
    await RisingEdge(dut.clk)

    # ----------------
    # INVALID (S=1 R=1)
    # ----------------
    dut.ui_in.value = 0b11
    await RisingEdge(dut.clk)

    # small delay to allow simulator finish cleanly
    await Timer(10, units="ns")
