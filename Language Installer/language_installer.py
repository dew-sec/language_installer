import subprocess

def install_java():
    """Install Java"""
    print("Installing Java...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "openjdk-11-jdk"])

def install_php():
    """Install PHP"""
    print("Installing PHP...")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "php7.4-fpm", "php7.4-mysql"])

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

def main():
    print("Language Installer Script")
    print("---------------------------")

    install_java()
    install_php()
    install_golang()
    install_cpp()
    install_nodejs()
    install_apache()
    install_git()

    print("Installation complete!")

if __name__ == "__main__":
    main()
