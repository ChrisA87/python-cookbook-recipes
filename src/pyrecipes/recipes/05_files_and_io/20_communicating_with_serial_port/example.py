"""
You want to read and write data over a serial port, typically to
interect wit some kind of harware device (e.g. a robot or sensor).
"""
import serial


def example_1():
    """For illustrative purposes only."""
    ser = serial.Serial(
        "/dev/tty.usbmodem641",  # Device name varies
        baudrate=9600,
        bytesize=8,
        parity="N",
        stopbits=1,
    )

    ser.write(b"G1 X50 Y50 Y50\r\n")
    resp = ser.readline()
    print(resp)


def main():
    pass


if __name__ == "__main__":
    main()
