from typing import Protocol


class DiagnosticUpdate(Protocol):
    def status_update(self) -> str:
        ...


def collect_diagnostics(device: DiagnosticUpdate) -> None:
    print("Connecting to diagnostics server.")
    status = device.status_update()
    print(f"Sending status update [{status}] to server.")
