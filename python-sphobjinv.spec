%global module sphobjinv

Name:		python-sphobjinv
Version:	2.3.1.3
Release:	1
Summary:	Toolkit to manipulate and inspect Sphinx objects.inv files
Group:		Development/Python
License:	MIT
URL:		https://github.com/bskinn/sphobjinv
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(fuzzywuzzy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Toolkit for manipulation and inspection of Sphinx objects.inv files


######################################
%prep
%autosetup -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info
# Remove shebangs
sed -i '1{/^#!/d}' src/sphobjinv/_vendored/fuzzywuzzy/*.py


%files
%{_bindir}/sphobjinv
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
%doc README.md
%license LICENSE.txt
