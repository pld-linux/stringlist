Summary:	Miscellaneous Memory and Configuration Function Library
Summary(pl):	Biblioteka funkcji konfiguracyjnych dla enlightenmenta
Name:		stringlist
Version:	0.3
Release:	5
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.debian.org/debian/dists/main/devel/libs/%{name}-%{version}.tar.bz2
URL:		http://mandrake.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The StringList library provides several miscellaneous sets of
functions for tracking memory usage, Enlightenment's configuration
language, file and string manipulations.

%description -l pl 
Biblioteka StringList umo©liwia rС©norodne ustawienia funkcji
konfiguracyjnych dla Enlightenmenta.

%package devel
Summary:	Header files and other resources for development
Summary(pl):	Pliki nagЁСwkowe i inne zasoby potrzebne
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files and other resources for development stringlist based
applications.

%description -l pl devel
Pliki nagСЁwkowe i inne zasoby potrzebne przy robieniu aplikacji
wykorzystujacych bibliotekЙ stringlist.

%package static
Summary:	Static stringlist library
Summary(pl):	Biblioteka statyczna stringlist
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static stringlist library.

%description -l pl static
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz NEWS.gz README.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
