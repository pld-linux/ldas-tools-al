Summary:	Abstraction layer for the ldas-tools package
Summary(pl.UTF-8):	Warstwa abstrakcji dla pakietu ldas-tools
Name:		ldas-tools-al
Version:	2.6.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.gz
# Source0-md5:	b6ed06cb12e88de3bc1ac1a6a3be31b8
URL:		https://wiki.ligo.org/Computing/LDASTools
BuildRequires:	boost-devel >= 1.67
BuildRequires:	cmake >= 3.2
BuildRequires:	doxygen
BuildRequires:	igwn-cmake-macros >= 1.5.0
BuildRequires:	ldas-tools-cmake >= 1.2.3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
# checked, but not used
#BuildRequires:	libframe-devel
#BuildRequires:	openssl-devel
#BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This provides a collection of classes and fuctions allowing for system
level abstraction as used by the LDAS Tools Suite.

%description -l pl.UTF-8
Zbiór klas i funkcji będących abstrakcją poziomu systemu, używany
przez zestaw narzędzi LDAS.

%package devel
Summary:	Header files for LDAS abstraction library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki abstrakcji LDAS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel >= 1.67
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for LDAS abstraction library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki abstrakcji LDAS.

%package static
Summary:	Static LDAS abstraction library
Summary(pl.UTF-8):	Statyczna biblioteka abstrakcji LDAS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LDAS abstraction library.

%description static -l pl.UTF-8
Statyczna biblioteka abstrakcji LDAS.

%package apidocs
Summary:	API documentation for LDAS abstraction library
Summary(pl.UTF-8):	Dokumentacja API biblioteki abstrakcji LDAS
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for LDAS abstraction library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki abstrakcji LDAS.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# Developer packaged as %doc, the other are subsets
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/{Administrator,Developer,User}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog.md README
%attr(755,root,root) %{_libdir}/libldastoolsal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldastoolsal.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libldastoolsal.so
%{_includedir}/ldastoolsal
%{_pkgconfigdir}/ldastoolsal.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libldastoolsal.a

%files apidocs
%defattr(644,root,root,755)
# Developer is superset of User and Administrator
%doc build/doc/Developer/html/{search,*.css,*.html,*.js,*.png}
