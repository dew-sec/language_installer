import subprocess

def install_java():
    """Install Java"""
    print("Installing Java...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "openjdk-11-jdk"])

def install_golang():
    """Install Go"""
    print("Installing Go...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "golang-go"])

def install_cpp():
    """Install C++"""
    print("Installing C++...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "build-essential"])

def install_nodejs():
    """Install Node.js"""
    print("Installing Node.js...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "nodejs"])

def install_apache():
    """Install Apache"""
    print("Installing Apache...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "apache2"])

def install_git():
    """Install Git"""
    print("Installing Git...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "git"])

def install_ruby():
    """Install Ruby"""
    print("Installing Ruby...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "ruby-full"])

def install_perl():
    """Install Perl"""
    print("Installing Perl...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "perl"])

def install_python3_dev():
    """Install Python 3 Dev"""
    print("Installing Python 3 Dev...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "python3-dev"])

def install_swift():
    """Install Swift"""
    print("Installing Swift...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "swift"])

def install_kotlin():
    """Install Kotlin"""
    print("Installing Kotlin...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "kotlin"])

def install_scala():
    """Install Scala"""
    print("Installing Scala...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "scala"])

def install_rust():
    """Install Rust"""
    print("Installing Rust...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "rustc"])

def install_haskell():
    """Install Haskell"""
    print("Installing Haskell...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "haskell-platform"])

def install_lisp():
    """Install Lisp"""
    print("Installing Lisp...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "sbcl"])

def install_scheme():
    """Install Scheme"""
    print("Installing Scheme...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "guile-2.2"])

def install_erlang():
    """Install Erlang"""
    print("Installing Erlang...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "erlang"])

def install_elixir():
    """Install Elixir"""
    print("Installing Elixir...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "elixir"])

def main():
    print("Language Installer Script")
    print("---------------------------")

    install_java()
    install_golang()
    install_cpp()
    install_nodejs()
    install_apache()
    install_git()
    install_ruby()
    install_perl()
    install_python3_dev()
    install_swift()
    install_kotlin()
    install_scala()
    install_rust()
    install_haskell()
    install_lisp()
    install_scheme()
    install_erlang()
    install_elixir()

if __name__ == "__main__":
    main()
