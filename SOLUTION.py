import os

class DocsTarget:
    """
    Represents the deduplicated 'docs' Make target.
    Encapsulates the shell command logic to ensure RUSTDOCFLAGS 
    are correctly passed to make warnings fatal.
    """

    def __init__(
        self,
        flags: str = '"-D warnings"',
        cmd: str = "cargo doc",
        workspace: str = "--workspace",
        no_deps: str = "--no-deps",
    ) -> None:
        self.flags = flags
        self.cmd = cmd
        self.workspace = workspace
        self.no_deps = no_deps

    def __str__(self) -> str:
        """
        Returns the exact shell line expected by 'make -n docs'.
        """
        return f"RUSTDOCFLAGS={self.flags} {self.cmd} {self.workspace} {self.no_deps}"

    def __repr__(self) -> str:
        """
        Useful for debugging object state.
        """
        return f"DocsTarget({self.__str__()})"


if __name__ == "__main__":
    target = DocsTarget()
    print(target)