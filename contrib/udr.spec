
Summary: UDT wrapper for rsync
#Description: UDR is a wrapper around rsync that enables rsync to use UDT.
Name: udr
Version: 0.9.4
Release: 1%{?dist}
License: Apache 2.0
Group: Applications/System
URL: https://github.com/LabAdvComp/UDR

# Create source tar file file by pulling the following URL
#   git clone https://github.com/LabAdvComp/UDR udr-<VERSION>
#   
Source: udr-%{version}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description 
UDR is a wrapper around rsync that enables rsync to use UDT.


%prep
%setup

%build
%{__make} 

%install
%{__rm} -rf %{buildroot} && %{__mkdir} -p %{buildroot}
echo "sourcedir=${RPM_SOURCE_DIR}/%{name}-%{version}"
%{__install} -D -m 755 ${RPM_BUILD_DIR}/%{name}-%{version}/src/udr %{buildroot}/%{_bindir}/udr

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.md LICENSE.txt
%{_bindir}/udr
