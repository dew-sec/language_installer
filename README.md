
---

# Language Installer for Zorin OS or Ubuntu based distributions

## Description

The Language Installer is a Python script designed to simplify the installation of various programming languages and development tools on Zorin OS. This script automates the installation of commonly used programming languages and tools in web and software development, including Java, Go, C++, Node.js, as well as server tools like Apache and Git. With expanded support, it now also includes languages such as Ruby, Perl, Swift, Kotlin, and more!

## Features

- **Automated Installation**: Installs multiple languages and tools with a single command.
- **Supports Multiple Languages**:
  - Java (OpenJDK)
  - Go (Golang)
  - C++ (build-essential)
  - Node.js
  - Apache (web server)
  - Git (version control tool)
  - Ruby
  - Perl
  - Python 3 Development (python3-dev)
  - Swift
  - Kotlin
  - Scala
  - Rust
  - Haskell
  - Lisp (SBCL)
  - Scheme (Guile)
  - Erlang
  - Elixir

## Prerequisites

- Zorin OS or other Ubuntu-based distributions.
- Python 3.x must be installed on your system.
- An active internet connection to download packages.

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dew-sec/language_installer.git
   cd language_installer
   ```

2. **Run the Script**:

   - Give execution permission to the script:

     ```bash
     chmod +x language_installer.py
     ```

   - Execute the script with superuser privileges:

     ```bash
     sudo ./language_installer.py
     ```

## Error Handling

The script includes error handling to assist users in identifying and resolving issues that may arise during the installation process. If an error occurs, an appropriate message will be printed to the console.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This script is licensed under the MIT License.

---
