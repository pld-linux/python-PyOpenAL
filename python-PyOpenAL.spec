%include	/usr/lib/rpm/macros.python
%define	pname	PyOpenAL
Summary:	Binding of OpenAL for Python
Summary(pl):	Interfejs OpenAL dla Pythona
Name:		python-PyOpenAL
Version:	0.1.3
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://oomadness.nekeme.net/downloads/%{pname}-%{version}.tar.gz
# Source0-md5:	2357d1d9ac1e99b0588bfc14d10fd9cd
URL:		http://oomadness.nekeme.net/en/pyopenal/
BuildRequires:	OpenAL-devel
BuildRequires:	python-devel
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binding of OpenAL for Python.

%description -l pl
Interfejs OpenAL dla Pythona.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pyopenal/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/pyopenal
