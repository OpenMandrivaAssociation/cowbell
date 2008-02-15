%define name	cowbell
%define version 0.2.7.1
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Music collection organizer and editor
Version: 	%{version}
Release: 	%{release}

Source:		http://more-cowbell.org/releases/%{name}-%{version}.tar.bz2
URL:		http://more-cowbell.org/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig ImageMagick
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
%configure2_5x
perl -p -i -e 's/lib\/cowbell/%{_lib}\/cowbell/g' Makefile
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

%post
%update_menus
		
%postun
%clean_menus

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

