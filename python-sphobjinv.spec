# Created by pyp2rpm-3.3.5
%global pypi_name sphobjinv

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2
Summary:        Sphinx objects.inv Inspection/Manipulation Tool
Group:          Development/Python
License:        MIT License
URL:            https://github.com/bskinn/sphobjinv
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
sphobjinv: Manipulate and inspect Sphinx objects.inv files **Current
Development Version:** **Most Recent Stable Release:** .. image::

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/sphobjinv
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
