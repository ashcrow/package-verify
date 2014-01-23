# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           package-verify
Version:        0.0.1
Release:        1%{?dist}
Summary:        Simple package verification tool

License:        GPLv3+
URL:            https://github.com/ashcrow/package-verify
Source0:        package_verify-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel, help2man


%description
Simple package verification tool.

%prep
%setup -q -n package_verify-%{version}


%build
%{__python} setup.py build
help2man --no-discard-stderr --no-info --version-string="%{version}" "%{__python} src/package_verify/script.py" | %{__sed} -e "s|SCRIPT.PY|PACKAGE-VERIFY|g" | %{__sed} -e "s|script.py|package-verify|" > %{name}.1

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
 
%files
%doc LICENSE README.md
# For noarch packages: sitelib
%{python_sitelib}/*
%{_bindir}/%{name}
%{_mandir}/man1/*.gz

%changelog
* Thu Jan 23 2014 Steve Milner <stevem@gnulinux.net> - 0.0.1-1
- Initial spec
