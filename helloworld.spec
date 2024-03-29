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
# Define the directory where the RPM package will be installed
install_dir=$RPM_BUILD_ROOT

# Copy the helloworld script to the install directory
mkdir -p $install_dir
install -m 0755 helloworld $install_dir/%{name}

%files
# Define the path to the installed helloworld script
/%{_bindir}/%{name}

%changelog
