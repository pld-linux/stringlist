Summary:	Miscellaneous Memory and Configuration Function Library
Summary(pl.UTF-8):	Biblioteka funkcji konfiguracyjnych dla enlightenmenta
Name:		stringlist
Version:	0.3
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://ftp.debian.org/debian/dists/main/devel/libs/%{name}-%{version}.tar.bz2
# Source0-md5:	a42e43f67e41a6eb52571034c95e0fb4
URL:		http://mandrake.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The StringList library provides several miscellaneous sets of
functions for tracking memory usage, Enlightenment's configuration
language, file and string manipulations.

%description -l pl.UTF-8
Biblioteka StringList umożliwia różnorodne ustawienia funkcji
konfiguracyjnych dla Enlightenmenta.

%package devel
Summary:	Header files and other resources for development
Summary(pl.UTF-8):	Pliki nagłówkowe i inne zasoby potrzebne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and other resources for development stringlist based
applications.

%description devel -l pl.UTF-8
Pliki nagółwkowe i inne zasoby potrzebne przy robieniu aplikacji
wykorzystujacych bibliotekę stringlist.

%package static
Summary:	Static stringlist library
Summary(pl.UTF-8):	Biblioteka statyczna stringlist
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static stringlist library.

%description static -l pl.UTF-8
Biblioteka statyczna stringlist.

%prep
%setup -q

%build
%configure2_13 \
	 --enable-shared \
	 --enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
