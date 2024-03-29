Name:       helloworld
Version:    1.0
Release:    1%{?dist}
Summary:    Hello World
License:    GPLv3+
BuildArch:  noarch

%description
Hello World!

%prep

%build

%install
# Create directory for installation
mkdir -p %{buildroot}/usr/bin

# Install the helloworld executable
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/helloworld

%files
/usr/bin/helloworld

%changelog
