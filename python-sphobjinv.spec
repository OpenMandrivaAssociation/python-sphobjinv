%global module sphobjinv

Name:		python-%{module}
Version:	2.3.1.2
Release:	1
Summary:	Toolkit to manipulate and inspect Sphinx objects.inv files
Group:		Development/Python
License:	MIT
URL:		https://github.com/bskinn/sphobjinv
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-fuzzywuzzy
BuildRequires:	python-pytest
BuildRequires:	python-setuptools
BuildRequires:	python-wheel

Requires:	python-attrs
Requires:	python-certifi
Requires:	python-jsonschema

%description
Toolkit for manipulation and inspection of Sphinx objects.inv files


######################################
%prep
%autosetup -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info
# Remove shebangs
sed -i '1{/^#!/d}' src/sphobjinv/_vendored/fuzzywuzzy/*.py

######################################
%build
%py3_build

######################################
%install
%py3_install

######################################
%files -n python-%{module}
%{_bindir}/sphobjinv
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.dist-info
%doc README.md
%license LICENSE.txt
