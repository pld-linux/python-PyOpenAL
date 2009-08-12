%define		pname	PyOpenAL
Summary:	Binding of OpenAL for Python
Summary(pl.UTF-8):	Interfejs OpenAL dla Pythona
Name:		python-%{pname}
Version:	0.1.6
Release:	3
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://download.gna.org/pyopenal/%{pname}-%{version}.tar.gz
# Source0-md5:	51992fc62df474614ea6eb724061f392
URL:		http://home.gna.org/oomadness/en/pyopenal/
BuildRequires:	OpenAL-devel
BuildRequires:	freealut-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binding of OpenAL for Python.

%description -l pl.UTF-8
Interfejs OpenAL dla Pythona.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyopenal/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/pyopenal
%{py_sitedir}/*.egg-info
