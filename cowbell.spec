%define name	cowbell
%define version 0.2.7.1
%define release 9

Name: 	 	%{name}
Summary: 	Music collection organizer and editor
Version: 	%{version}
Release: 	%{release}1

Source:		http://more-cowbell.org/releases/%{name}-%{version}.tar.bz2
URL:		https://more-cowbell.org/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig imagemagick
BuildRequires:	mono-devel gtk-sharp2 glade-sharp2
BuildRequires:	taglib-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  desktop-file-utils

%description
Do you ever pull your hair out trying to hand-edit all your tags with some
arcane editor? Tell your inner OCD to take a hike because Cowbell is coming
to town.

Cowbell is an elegant music organizer intended to make keeping your
collection tidy both fun and easy.

Infused with Amazon Web Services SOAP-fu, Cowbell can whip your music
platoon into shape without even getting your boots muddy. And, if that isn't
enough to make you want to rush to the Download link, Cowbell can also
snatch album art and rename your music files like a pro.

%prep
%setup -q

%build
perl -p -i -e 's/lib\/cowbell/%{_lib}\/cowbell/g' Makefile* cowbell.in
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Audio" \
  --add-category="Recorder" \
  --add-category="AudioVideo" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 resources/%name.svg $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 resources/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 resources/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_libdir}/%name
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Mon Feb 01 2010 Jérôme Brenier <incubusss@mandriva.org> 0.2.7.1-8mdv2010.1
+ Revision: 499152
- fix path in cowbell.in too
- do path fixes before configure

* Sun Jan 31 2010 Jérôme Brenier <incubusss@mandriva.org> 0.2.7.1-7mdv2010.1
+ Revision: 498916
- fix License tag

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.2.7.1-6mdv2010.0
+ Revision: 425049
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.7.1-5mdv2009.0
+ Revision: 243689
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Feb 15 2008 Götz Waschk <waschk@mandriva.org> 0.2.7.1-3mdv2008.1
+ Revision: 168999
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.7.1-2mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cowbell


* Wed Sep 13 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.7.1-2mdv2007.0
- XDG

* Wed May 24 2006 Austin Acton <austin@mandriva.org> 0.2.7.1-1mdk
- New release 0.2.7.1

* Wed May 03 2006 Emmanuel Andry <eandry@free.fr> 0.2.7-1mdk
- New release 0.2.7

* Fri Mar 03 2006 Austin Acton <austin@mandriva.org> 0.2.6.1-1mdk
- New release 0.2.6.1

* Sat Dec 17 2005 Austin Acton <austin@mandriva.org> 0.2.5.1-1mdk
- New release 0.2.5.1

* Fri Nov 18 2005 Austin Acton <austin@mandriva.org> 0.2.5-2mdk
- fix buildreuires
- lib64 fix

* Fri Nov 18 2005 Austin Acton <austin@mandriva.org> 0.2.5-1mdk
- New release 0.2.5

* Thu Oct 06 2005 Austin Acton <austin@mandriva.org> 0.2.4-1mdk
- New release 0.2.4

* Wed Sep 28 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.3-3mdk
- Fix BuildRequires

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 0.2.3-2mdk
- rebuild for new gtk-sharp2

* Sat Aug 13 2005 Austin Acton <austin@mandriva.org> 0.2.3-1mdk
- New release 0.2.3

* Mon Aug 8 2005 Austin Acton <austin@mandriva.org> 0.2.2-1mdk
- 0.2.2
- source URL

* Sun Jul 24 2005 Austin Acton <austin@mandriva.org> 0.2-1mdk
- initial package
