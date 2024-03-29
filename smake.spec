Summary:	A make replacement with Makefile hierarchy support and priority based target overriding
Summary(pl.UTF-8):	Zamiennik make z obsługą hierarchii i przykrywaniem opartym na priorytetach
Name:		smake
Version:	1.3.2
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://www.engelschall.com/sw/smake/%{name}-%{version}.tar.gz
# Source0-md5:	d4c34b912a5863ae662b9f9ab3c4bd98
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.engelschall.com/sw/smake/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful mechanism to generate standard Makefiles out of skeleton
Makefiles which only provide the essential parts. The missing stuff
gets automatically filled in by shared include files. A great scheme
to create a huge Makefile hierarchy and to keep it consistent for the
time of development. The trick is that it merges the skeleton and the
templates in a priority-driven way. The idea is taken from X
Consortium's Imake, but the goal here is not inherited system
independency, the goal is consistency and power without the need of
manually maintaining a Makefile hierarchy.

%description -l pl.UTF-8
Potężny mechanizm do generowania plików Makefile ze szkieletowych
Makefile, dostarczających jedynie podstawowe fragmenty. Brakująca
treść jest automatycznie wypełniana poprzez współdzielone dołączane
pliki. Dobry schemat do tworzenia wielkiej hierarchii plików Makefile
i utrzymywania ich w spójności przy tworzeniu oprogramowania. Trick
polega na tym, że smake łączy szkielet i szablony w sposób oparty na
priorytetach. Idea pochodzi z Imake X Consortium, ale celem nie jest
odziedziczenie niezależności od systemu, lecz spójność i duże
możliwości bez potrzeby ręcznego utrzymywania hierarchii plików
Makefile.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
export SHTOOL="./etc/shtool"
chmod +x "./etc/shtool"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo ".so smake.1" > $RPM_BUILD_ROOT%{_mandir}/man1/smkmf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/smake
%{_libdir}/smake/smk.*
%{_mandir}/man1/*1.*
