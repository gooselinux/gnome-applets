%define glib2_version 2.15.3
%define pango_version 1.2.0
%define gtk2_version 2.6.0
%define libgnome_version 2.8.0
%define libgnomeui_version 2.8.0
%define libglade_version 2.4.0
%define gnome_panel_version 2.20.1-5
%define libgtop2_version 2.12.0
%define gail_version 1.2.0
%define libbonoboui_version 2.3.0
%define gstreamer_version 0.10.14
%define gstreamer_plugins_version 0.10.14
%define gstreamer_plugins_good_version 0.10.6
%define libxklavier_version 4.0
%define libwnck_version 2.9.3
%define libgnome_desktop_version 2.11.1
%define gnome_utils_version 2.8.1
%define dbus_version 0.90
%define dbus_glib_version 0.70
%define libnotify_version 0.3.2
%define pygobject_version 2.6
%define pygtk_version 2.6
%define gnome_python_version 2.10
%define gconf_version 2.14.0
%define libgnomekbd_version 2.27.4

%define po_package gnome-applets-2.0

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define build_stickynotes 0

Summary:        Small applications for the GNOME panel
Name:		gnome-applets
Version:	2.28.0
Release: 	7%{?dist}
Epoch:          1
License:	GPLv2+ and GFDL
Group:          User Interface/Desktops
URL:		http://www.gnome.org/
Source: 	http://download.gnome.org/sources/%{name}/2.28/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch2:		gnome-applets-2.23.3-use-builtin-apm.patch
Patch11:        gnome-applets-2.15.1.1-dont-require-display.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=424639
Patch31:        gnome-applets-2.18.0-fix-find.patch

# do the nullapplet dance for battstat
Patch40:	gnome-applets-null-battstat.patch
# and keep the mixer hidden away from the add to panel dialog
Patch41:	gnome-applets-no-mixer-icon.patch
# do the nullapplet dance for stickynotes
Patch42:	stickynotes-null.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=599728
Patch44:	seriesid-clash.patch

# make trashapplet docs show up in rarian/yelp
Patch45:        gnome-applets-doc-category.patch

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=575714
Patch46:        gnome-applets-translations.patch

BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk2-devel >= %{gtk2_version}
BuildRequires:  libgnomeui-devel >= %{libgnomeui_version}
BuildRequires:  libgnome-devel >= %{libgnome_version}
BuildRequires:  gnome-panel-devel >= %{gnome_panel_version}
BuildRequires:  libglade2-devel >= %{libglade_version}
BuildRequires:  libgtop2-devel >= %{libgtop2_version}
BuildRequires:  pango-devel >= %{pango_version}
BuildRequires:  gail-devel >= %{gail_version}
BuildRequires:  libxklavier-devel >= %{libxklavier_version}
BuildRequires:  gstreamer-devel >= %{gstreamer_version}
BuildRequires:  gstreamer-plugins-base-devel >= %{gstreamer_plugins_version}
BuildRequires:  gstreamer-plugins-good-devel >= %{gstreamer_plugins_good_version}
BuildRequires:  /usr/bin/automake
BuildRequires:  libbonoboui-devel >= %{libbonoboui_version}
BuildRequires:  libwnck-devel >= %{libwnck_version}
BuildRequires:  gnome-desktop-devel >= %{libgnome_desktop_version}
BuildRequires:  gnome-utils >= %{gnome_utils_version}
BuildRequires:  libnotify-devel >= %{libnotify_version}
BuildRequires:  pygobject2-devel >= %{pygobject_version}
BuildRequires:  pygtk2-devel >= %{pygtk_version}
BuildRequires:  gnome-python2-devel >= %{gnome_python_version}
BuildRequires:  gnome-python2-applet
BuildRequires:  gucharmap-devel
BuildRequires:  dbus-devel >= %{dbus_version}
BuildRequires:  dbus-glib-devel >= %{dbus_glib_version}
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  which
BuildRequires:  libtool autoconf gettext intltool
BuildRequires:  pkgconfig
BuildRequires:  gnome-icon-theme
BuildRequires:  libgnomekbd-devel >= %{libgnomekbd_version}
BuildRequires:  libxslt
# for patch 39
BuildRequires:  NetworkManager-devel
BuildRequires:  libgweather-devel >= 2.22.1
# For cpufreq
BuildRequires: 	dbus-devel
BuildRequires:  polkit-devel >= 0.92

Requires:	gnome-panel >= %{gnome_panel_version}
Requires:	libxklavier >= %{libxklavier_version}
Requires:	gstreamer-plugins-base >= %{gstreamer_plugins_version}
Requires:	gstreamer-plugins-good >= %{gstreamer_plugins_good_version}

Requires:	dbus >= %{dbus_version}

Requires(pre): GConf2 >= %{gconf_version}
Requires(preun): GConf2 >= %{gconf_version}
Requires(post): GConf2 >= %{gconf_version}

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

# For invest-applet
Requires:	gnome-python2-applet
Requires:	gnome-python2-libegg

Obsoletes:      battstat_applet
Obsoletes:      gnome-cpufreq-applet

# since we are installing .pc files
Requires:	pkgconfig

%description
The gnome-applets package contains small applications which generally
run in the background and display their output to the GNOME  panel.
It includes a clock, a character palette, load monitors, little toys,
and more.

%prep
%setup -q
%patch2 -p1 -b .use-builtin-apm
%patch11 -p1 -b .dont-require-display

%patch31 -p1 -b .fix-find
%patch40 -p1 -b .battstat-null
%patch41 -p1 -b .no-mixer-icon
%patch42 -p1 -b .stickynotes-null

%patch44 -p1 -b .seriesid
%patch45 -p1 -b .doc-category
%patch46 -p2 -b .translations

autoreconf -i -f


%build
%configure			\
	--enable-suid=no 	\
%if %{build_stickynotes}
	--enable-stickynotes	\
%endif
	--disable-battstat	\
	--disable-scrollkeeper 	\
	--enable-mini-commander \
	--enable-gtk-doc

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
intltool-update --pot
for p in *.po; do
  msgmerge $p %{po_package}.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# save space by linking identical images in translated docs
for helpdir in $RPM_BUILD_ROOT%{_datadir}/gnome/help/*; do
  for f in $helpdir/C/figures/*.png; do
    b="$(basename $f)"
    for d in $helpdir/*; do
      if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
        g="$d/figures/$b"
        if [ -f "$g" ]; then
          if cmp -s $f $g; then
            rm "$g"; ln -s "../../C/figures/$b" "$g"
          fi
        fi
      fi
    done
  done
done

%find_lang %{po_package} --all-name --with-gnome

# Clean up unpackaged files
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper
rm -f $RPM_BUILD_ROOT%{_libdir}/libgweather.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libgweather.a

# drop non-XKB support files
rm -rf $RPM_BUILD_ROOT%{_datadir}/xmodmap


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update -q
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule                                        \
	    %{_sysconfdir}/gconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas            \
	    %{_sysconfdir}/gconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/gconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/gconf/schemas/gweather.schemas                  \
	    %{_sysconfdir}/gconf/schemas/mini-commander-global.schemas     \
	    %{_sysconfdir}/gconf/schemas/mini-commander.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/gconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/gconf/schemas/multiload.schemas > /dev/null
%{_libexecdir}/gnome-applets/mc-install-default-macros >& /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule                                    \
	    %{_sysconfdir}/gconf/schemas/battstat.schemas                  \
	    %{_sysconfdir}/gconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas            \
	    %{_sysconfdir}/gconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/gconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/gconf/schemas/gswitchit.schemas                 \
	    %{_sysconfdir}/gconf/schemas/gweather.schemas                  \
	    %{_sysconfdir}/gconf/schemas/mini-commander-global.schemas     \
	    %{_sysconfdir}/gconf/schemas/mini-commander.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/gconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/gconf/schemas/multiload.schemas >& /dev/null || :
  if [ -f %{_sysconfdir}/gconf/schemas/battstat.schemas ]; then
    gconftool-2 --makefile-uninstall-rule 				\
	    %{_sysconfdir}/gconf/schemas/battstat.schemas >& /dev/null || :
  fi
  if [ -f %{_sysconfdir}/gconf/schemas/mixer.schemas ]; then
     gconftool-2 --makefile-uninstall-rule 				\
     	     %{_sysconfdir}/gconf/schemas/mixer.schemas >& /dev/null || :
  fi
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule                                    \
	    %{_sysconfdir}/gconf/schemas/charpick.schemas                  \
	    %{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas            \
	    %{_sysconfdir}/gconf/schemas/drivemount.schemas                \
	    %{_sysconfdir}/gconf/schemas/geyes.schemas                     \
	    %{_sysconfdir}/gconf/schemas/gweather.schemas                  \
	    %{_sysconfdir}/gconf/schemas/mini-commander-global.schemas     \
	    %{_sysconfdir}/gconf/schemas/mini-commander.schemas            \
%if %{build_stickynotes}
	    %{_sysconfdir}/gconf/schemas/stickynotes.schemas               \
%endif
	    %{_sysconfdir}/gconf/schemas/multiload.schemas >& /dev/null || :
fi

%postun
/sbin/ldconfig
scrollkeeper-update -q
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{po_package}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome-applets
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{python_sitelib}/invest/
%{_libexecdir}/accessx-status-applet
%{_libexecdir}/charpick_applet2
%{_libexecdir}/cpufreq-applet
%{_libexecdir}/drivemount_applet2
%{_libexecdir}/geyes_applet2
%{_libexecdir}/gnome-applets/
%{_libexecdir}/gnome-keyboard-applet
%{_libexecdir}/gweather-applet-2
%{_libexecdir}/mini_commander_applet
%{_libexecdir}/multiload-applet-2
%{_libexecdir}/null_applet

%if %{build_stickynotes}
%{_libexecdir}/stickynotes_applet
%endif

%{_libexecdir}/trashapplet
%{_libexecdir}/invest-applet
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service


%changelog
* Tue Aug 03 2010 Parag Nemade <pnemade AT redhat.com> 2.28.0-7
- Resolves:rh#575714: Update translations.
- Use updated patch gnome-applets-translations.patch

* Fri Jul 02 2010 Ray Strode <rstrode@redhat.com> 2.28.0-6
- rebuild
  Resolves: #609758

* Tue May 11 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-5
- Updated translations
Resolves: #575714

* Mon May  3 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-4
- Make trashapplet docs show up in yelp
Resolves: #588564

* Fri Jan 29 2010 Ray Strode <rstrode@redhat.com> 2.28.0-3
- Drop modem lights

* Tue Oct 27 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.28.0-2
- Fix a help file seriesid clash between accessx-status and invest-applet

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.28.0-1
- Update to 2.28.0

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.91-1
- 2.27.91

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.4-1
- Update to 2.27.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.27.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-5
- Rebuild against new libgnomekbd

* Mon Jul 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-4
- Fix PolicyKit 1 patch

* Tue Jun 30 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-3
- Rebuild against new libxklavier

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-2
- Drop sticky notes, now that we have gnotes

* Wed Jun 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.3-1
- Update to 2.27.3

* Sat Jun 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-3
- Drop unneeded direct dependencies

* Wed Jun 10 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-2
- Port to PolicyKit 1

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.27.2-1
- Update to 2.27.2
- http://download.gnome.org/sources/gnome-applets/2.27/gnome-applets-2.27.2.news

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-3
- Don't drop schemas translations from po files

* Wed Apr 15 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-2
- Make gweather network status tracking work

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.26.1-1
- Update to 2.26.1

* Sun Mar 29 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-4
- Make cpufreq applet work (#492741)

* Sat Mar 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-3
- Make the invest applet work

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-2
- Support https in minicommander (#490387)

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.92-1
- Update to 2.25.92

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.25.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.91-2
- Update to 2.25.91

* Fri Feb  6 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.90-3
- Keep the dead mixer applet from haunting the add to panel dialog

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.90-1
- Update to 2.25.90

* Wed Jan 21 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.4-2
- Fix trash applet not starting up

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.4-1
- Update to 2.25.4

* Sun Jan 11 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.3-3
- Fix the nullappletification of the mixer applet

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 1:2.25.3-2
- Update to 2.25.3

* Sat Dec 20 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.2-4
- Update to 2.25.2

* Fri Dec 19 2008 - Bastien Nocera <bnocera@redhat.com> - 1:2.25.1-8
- Fix battstat nullification

* Fri Dec 19 2008 - Bastien Nocera <bnocera@redhat.com> - 1:2.25.1-7
- Remove the mixer applet

* Fri Dec 19 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-5
- Fix the build

* Thu Dec 18 2008 Jon McCann <jmccann@redhat.com> - 1:2.25.1-5
- Rebuild for gnome-desktop

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:2.25.1-4
- Rebuild for Python 2.6

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-4
- Improve description

* Fri Nov 21 2008 Ray Strode <rstrode@redhat.com> - 1:2.25.1-3
- Install modemlights schema (bug 417031)

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-2
- Rebuild

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.25.1-1 
- Update to 2.25.1

* Tue Oct 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.1-1
- Update to 2.24.1

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-5
- Fix some missing translations

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-4
- Save space

* Fri Sep 26 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-3
- Small improvement to the drivemount applet

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0.1-2
- Update to 2.24.0.1

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.24.0-2
- Update to 2.24.0

* Tue Sep 16 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.92-2
- Plug a leak in the trash applet

* Tue Sep  9 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.92-1
- Update to 2.23.92

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.91-1
- Update to 2.23.91

* Fri Aug 29 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.90-2
- Plug a memory leak in the keyboard applet

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.90-1
- Update to 2.23.90

* Fri Aug  8 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.4-2
- Undecorate the mixer popup 

* Mon Aug  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.4-1
- Update to 2.23.4

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.23.3-3
- fix license tag

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.3-1
- Update to 2.23.3

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.2-2
- Rebuild

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.23.2-1
- Update to 2.23.2
- Drop upstreamed patches

* Tue May  6 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-3
- Drop gnome-netstatus dependency (#445059)

* Wed Apr 23 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-2
- Reduce the trash icon size (#438620)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.1-1
- Update to 2.22.1

* Fri Apr  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.0-2
- Fix a bug in the keyboard accessibility applet

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.91-1
- Update to 2.21.91

* Thu Jan 31 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-5
- Rebuild against new libxklavier

* Fri Jan 25 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-4
- Port trash applet to gvfs
- Remove gnome-vfs dependency in gweather

* Mon Jan 21 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-3
- Fix the invest applet on vertical panels

* Sun Jan 20 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-2
- Make the weather applet find locations.xml again

* Wed Jan 16 2008 Matthias Clasen <mclasen@redhat.com> - 1:2.21.4-1
- Update to 2.21.4

* Sun Dec  9 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.21.2-2
- Silence the %%post script

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.21.2-1
- Update to 2.21.2
- Drop the battstat applet 

* Mon Oct 29 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-10
- Fix a number of problems in the weather applet

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-9
- Rebuild against new dbus-glib

* Sun Oct 21 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-8
- Update weather info when going online

* Fri Oct 12 2007 - Bastien Nocera <bnocera@redhat.com> - 1:2.20.0-7
- Update out-of-sync patch to handle mute properly (#320451)

* Thu Sep 27 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-6
- Fix a memory leak in the mixer preferences

* Tue Sep 25 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.20.0-5
- Fix possible crasher in the mixer messages when we receive an
  unhandled message (#302881)

* Sat Sep 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.2.20.0-4
- Build modemlights applet again (#301601)

* Sat Sep 22 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-3
- Make the gweather.pc file less useless

* Thu Sep 20 2007 - Bastien Nocera <bnocera@redhat.com> - 1:2.20.0-2
- Add patch to avoid the volume scale getting out-of sync with the 
  real hardware volume

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.91-1
- Update to 2.19.91

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1:2.19.1-8
- Rebuild for build ID

* Sun Aug 12 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-7
- Fix Requires

* Sun Aug 12 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-6
- Stop the mixer applet from polling the volume

* Sun Aug  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-5
- Use %%find_lang for help files, too
- Update the license field

* Sun Aug  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-4
- gswitchit.schemas does not exist anymore

* Thu Aug  2 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-3
- Waste less space in Locations.xml

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-2
- Fix scriptlets 

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.1-1
- Update to 2.19.1

* Tue Jul 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.0-2
- Rebuild

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.19.0-1
- Update to 2.19.0
- Drop modemlights, since it doesn't build anymore

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-13
- Another directory ownership fix

* Fri Jul  6 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-12
- Fix a directory ownership issue

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-11
- Fix #237058

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-10
- Rebuild again

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-9
- Rebuild against new libwnck

* Mon May 21 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-8
- Split off a -devel package

* Tue Apr 10 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-7
- Fix a leak in the keyboard indicator applet

* Sat Mar 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-6
- Fix the bug-buddy support of the accessx status applet

* Sat Mar 31 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-5
- Add bug-buddy support to the keyboard indicator applet

* Fri Mar 30 2007 Ray Strode <rstrode@redhat.com> - 1:2.18.0-4
- make gweather applet preferences find feature work slightly
  better (bug 209488)

* Wed Mar 28 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-3
- Remove non-XKB support files to save space

* Wed Mar 21 2007 Ray Strode <rstrode@redhat.com> - 1:2.18.0-2
- rerun intltoolize to get latest version

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.18.0-1
- Update to 2.18.0
- Drop upstreamed patch

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.17.90-1
- Update to 2.17.90

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.17.1-1
- Update to 2.17.1

* Wed Jan 10 2007 Ray Strode <rstrode@redhat.com> - 1:2.16.2-6
- fix null applet error on login for new users (bug 222104)

* Tue Dec 12 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.2-5
- fix mixer applet error on login for new users (bug 217919)

* Sat Dec  9 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-4
- Small spec file cleanups

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1:2.16.2-3
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-2
- Fix the trashapplet opening a window on the wrong screen (#218447)

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.2-1
- Update to 2.16.2
- Drop obsolete patches

* Thu Nov 16 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-5
- Fix muted icon in mixer again

* Mon Nov  6 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.1-4
- s/verion/version/ in dbus glib build requires

* Fri Nov  3 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-3
- Silence %%pre

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-2
- Make the cpufreq applet pick up preference changes (#209168)

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.1-1
- Update to 2.16.1
- Drop upstreamed patches

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-11
- Fix scripts according to packaging guidelines

* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-10
- Fix up requirements (#202549)

* Sat Oct 14 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-9
- Fix muting in the mixer applet (#208660)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1:2.16.0.1-7
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Ray Strode <rstrode@redhat.com> - 1:2.16.0.1-6
- Don't ask for password when changing CPU frequency

* Mon Sep 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-5
- Fix a segfault in the keyboard indicator applet

* Fri Sep 15 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-4
- Fix some icon size issues in the trash applet

* Sun Sep 10 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-3
- Make stickynotes not wake up 10 times per second (#205909)

* Fri Sep  8 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-2
- Fix the resizing behaviour of the mixer applet

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0.1-1.fc6
- Update to 2.16.0.1

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.16.0-1.fc6
- Update to 2.16.0

* Fri Sep  1 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-6.fc6
- Make the battstat applet poll less often (204858)

* Mon Aug 28 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-5.fc6
- Make cpufreq-selector use the config-utils pam policy

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-4.fc6
- Fix some redraw issues in the keyboard capplet

* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-3.fc6
- More keyboard drawing improvements

* Thu Aug 24 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-2.fc6
- Various improvements for the keyboard applet
 
* Tue Aug 22 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.90-1.fc6
- Update to 2.15.90
- Drop upstreamed patches
- Add a %%preun script
- Require pkgconfig

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-2.fc6
- Make the invest applet work

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.3-1.fc6
- Update to 2.15.3

* Tue Aug  8 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.2-4.fc6
- destroy about dialog on close (bug 197975)

* Sat Aug  5 2006 Caolan McNamara <caolanm@redhat.com> - 1:2.15.2-3.fc6
- rebuild against new gucharmap

* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.2-2.fc6
- Fix the multiload schema

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.2-1.fc6
- Update to 2.15.2

* Wed Aug  2 2006 Ray Strode <rstrode@redhat.com> - 1:2.15.1.1-7
- don't require a display to build invest applet (bug 200970).
  Problem discovered by Nalin Dahyabhai <nalin@redhat.com>

* Sat Jul 29 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-6
- Require gnome-python2-libegg for invest applet (#200640)

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1:2.15.1.1-5
- Add BR for dbus-glib-devel

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-4
- Rebuild against dbus

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.15.1.1-3.1
- rebuild

* Fri Jul  7 2006 Matthias Clasen <mclasen@redhat.com> - 1:2.15.1.1-3
- Try to make the invest applet actually work

* Thu Jun 22 2006 Jeremy Katz <katzj@redhat.com> - 1:2.15.1.1-2
- fix invest applet location

* Mon Jun 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.1.1-1
- Update to 2.15.1.1

* Thu Jun 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-5
- Rebuild against new libxklavier

* Thu Jun  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-4
- Explicitly list the applets to be included

* Tue Jun  6 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-3
- Rebuild

* Sun May 28 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1
- Update patches

* Tue Mar 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-3
- apply patch

 * Tue Mar 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-2
- export symbols in gswitchit applet so applet plugins 
  work (bug 187168)

* Sun Mar 12 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- update to 2.14.0

* Thu Mar  9 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-8
- s/divemount/drivemount/

* Thu Mar  9 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-7
- remove some bad trailing spaces introduced in 2.13.90-6

* Wed Mar  8 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-6
- improve package installation time by running gconftool-2 only
  once in %%post

* Wed Mar  8 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.90-5
- Fix a crash in the mixer applet (#184285, #182957)

* Tue Mar 7 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-4
- ref some objects given to us by gstreamer

* Wed Mar 1 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-3
- More stock ticker fun (bug 179528)

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.13.90-2
- BuildRequires: which

* Sun Feb 26 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.90-1
- Update to 2.13.90

* Thu Feb 23 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-4
- Make the stock ticker work with gcc 4.1 (#179528)

* Sat Feb 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-3
- Remove a warning from the stock ticker applet

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-2
- Build with --enable-mini-commander

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-1
- Update to 2.13.4

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.3-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.13.3-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb 01 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-4
- Fix an overflow in the weather applet

* Tue Jan 31 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-3
- Update gstreamer requires

* Tue Jan 31 2006 Matthias Clasen <mclasen@redhat.com> 2.13.3-1
- Update to 2.13.3

* Wed Jan 18 2006 Matthias Clasen <mclasen@redhat.com> 2.13.2-2
- BuildRequire gnome-doc-utils

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> 2.13.2-1
- Update to 2.13.2

* Fri Jan 05 2006 John (J5) Palmieri <johnp@redhat.com> 2.13.1-4
- GStreamer has been split into gstreamer08 and gstreamer (0.10) packages
  we need gstreamer08 for now

* Wed Jan 04 2006 Matthias Clasen <mclasen@redhat.com> 2.13.1-3
- Rebuild against new libgtop

* Fri Dec 16 2005 Matthias Clasen <mclasen@redhat.com> 2.13.1-2
- Rebuild against new libgtop

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.1-1
- Update to 2.13.1
- Update file lists

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 2.12.2-1.1
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> 2.12.2-1
- Update to 2.12.2

* Thu Dec 01 2005 John (J5) Palmieri <johnp@redhat.com> - 1:2.12.1-4
- rebuild for new dbus

* Mon Nov 14 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-3
- build correct command string for cpufreq-selection. Fix
  spotted by Ingo Schaefer <ingo@ingo-shaefer.de> (Bug 164147).

* Thu Oct 20 2005 Ray Strode <rstrode@redhat.com> - 1:2.12.1-2
- require libgtop2 >= 2.12.0, bug 171285

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.1-1
- Update to 2.12.1

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> - 1:2.12.0-1
- Update to 2.12.0, drop upstreamed patches

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 1:2.11.91-5
- fun with auto* to really get the build working

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 1:2.11.91-4
- patch from upstream cvs to fix build with new pango (bgo #313368)

* Tue Aug 16 2005 Warren Togami <wtogami@redhat.com> - 1:2.11.91-3
- rebuild for new cairo

* Thu Aug 11 2005 Ray Strode <rstrode@redhat.com> 1:2.11.91-2
- disable scrollkeeper database updates
- add omf files to package list
- require gnome-utils for gucharmap/charpick integration

* Wed Aug 10 2005 Ray Strode <rstrode@redhat.com> 1:2.11.91-1
- New upstream version

* Fri Aug  5 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.2-2
- New upstream version

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.1-2
- Rebuilt

* Fri Jul  8 2005 Matthias Clasen <mclasen@redhat.com> 1:2.11.1-1
- Update to 2.11.1

* Fri Jul  1 2005 Mark McLoughlin <markmc@redhat.com> 1:2.10.1-10
- Backport from HEAD patch to remove lame warning dialog when the
  mixer applet can't find a mixer device

* Fri May 27 2005 Bill Nottingham <notting@redhat.com> 1:2.10.1-9
- remove setuid bit from cpufreq-selector, usermode-ify it

* Thu May 19 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-8
- Install modemlights gconf schema (bug 157764).

* Fri May 13 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-7
- Don't disable battstat on some platforms (bug 157683).

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1:2.10.1-6
- silence %%post

* Tue Apr 26 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-5
- Add back old patch to change ppp connect/disconnect commands
  (bug 147675)

* Wed Apr 20 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-4
- Use builtin copy of apmlib instead of adding an external dependency
  (bug 155125)

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-3
- Apply patch from Jan de Groot <jan@jgc.homeip.net> to
  silence scrollkeeper noise (bug 152236)

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-2
- Add Obsoletes: gnome-cpufreq-applet (bug 154853)

* Thu Apr  7 2005 Ray Strode <rstrode@redhat.com> 1:2.10.1-1
- update to 2.10.1
- actually build the old modemlights that were added in 2.10.0-4

* Tue Apr  5 2005 Ray Strode <rstrode@redhat.com> 1:2.10.0-5
- Don't use %%postun -p optimization now that we do more than
  just /sbin/ldconfig in %%postun (bug 152236)

* Mon Apr  4 2005 Ray Strode <rstrode@redhat.com> 1:2.10.0-4
- use old modemlights applet that doesn't depend on gnome-system-tools

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>  2.10.0-3
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 2.10.0-2
- Update the GTK+ theme icon cache on (un)install

* Wed Mar 16 2005 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1
- Rebuild against new libwnck
- Update to 2.10.0
- Drop upstreamed patch

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 1:2.9.6-2
- Stop libgswitchit using -Werror
- Rebuild with gcc4

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.6-1
- Update to 2.9.6

* Wed Feb  9 2005 Mark McLoughlin <markmc@redhat.com> 2.9.5-4
- Add patch for mixer crash - #147282.
  Thanks Neil Paris for tracking down.

* Fri Feb  4 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.5-2
- Fix schemas list (#146880, #147011)

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.5-1
- Update to 2.9.5

* Sun Jan 30 2005 Florian La Roche <laroche@redhat.com>
- rebuild against new libs

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.0-5
- Add patch to fix crash with gweather preferences (#134572)

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.0-4
- Fix mixer icons bugs - #134224 and #134773

* Wed Sep 29 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-3
- Add new icons from upstream

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-2
- Remove the wireless applet and add patch to use the netstatus
  applet for backwards compat. bug #131652.

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0

* Wed Sep  1 2004 Mark McLoughlin <markmc@redhat.com> 2.7.3-2
- Rebuild

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.3-1
- Update to 2.7.3

* Fri Aug 27 2004 Mark McLoughlin <markmc@redhat.com> 2.7.2-2
- Run mc-install-default-macros in %%post
- Fixed small-volume patch from Nathan Fredrickson <nathan@silverorange.com>

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 2.7.2-1
- Update to 2.7.2

* Wed Aug 11 2004 Mark McLoughlin <markmc@redhat.com> 2.7.1-2
- Remove reference to cdplayer.schemas which has been removed (bug #129490)

* Thu Aug  5 2004 Mark McLoughlin <markmc@redhat.com> 2.7.1-1
- Update to 2.7.1
- Remove battstat-arg patch - upstream now

* Wed Jul 21 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.2.1-2
- rebuild

* Wed Jul 21 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.2.1-1
- Update to 2.6.2.1
- Re-do the way we decide whether to build the battstat applet.
  Should fix 122379
- Remove some patches that have gone upstream

* Tue Jun 22 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.0-8
- Fix typo with apmd requires

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
- Remove ifarch'd buildrequires on apmd

* Thu May 05 2004 Nils Philippsen <nphilipp@redhat.com> 1:2.6.0-5
- fix #120354 (mixer applet forgets channel settings)

* Thu Apr 29 2004 Karsten Hopp <karsten@redhat.de> 1:2.6.0-4
- fix error during update on s390(x) due to missing battery applet

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 1:2.6.0-3
- Build battstat on ppc too

* Wed Apr 14 2004 Alex Larsson <alexl@redhat.com> 1:2.6.0-2
- Add gswitchit.schemas to SCHEMAS

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-1
- Update to 2.6.0

* Tue Mar 16 2004 Jeremy Katz <katzj@redhat.com> 1:2.5.7-4
- rebuild for new gstreamer

* Thu Mar 11 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-3
- Update Requires/BuildRequires to include gstreamer-plugins

* Thu Mar 11 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-2
- Rebuild

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 2.5.7-1
- Update to 2.5.7
- Add gnome-panel-devel BuildRequires

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.6-1
- update to 2..5.6

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Alexander Larsson <alexl@redhat.com> 1:2.5.4-1
- update to 2.5.4

* Fri Oct  3 2003 Alexander Larsson <alexl@redhat.com> 1:2.4.1-1
- 2.4.1

* Wed Aug 27 2003 Alexander Larsson <alexl@redhat.com> 1:2.3.7-1
- Add missing schemas to post (fixes #102710)
- Update to 2.3.7
- Add ifnarch apmd buildreq

* Mon Aug 18 2003 Alexander Larsson <alexl@redhat.com> 1:2.3.6-1
- update for gnome 2.3

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 1:2.2.2-3
- require the newer libgtop2 so it rebuilds vs. correct soname

* Fri Jul 18 2003  <timp@redhat.com> 1:2.2.2-2
- rebuild against new libgtop

* Mon Jul  7 2003 Havoc Pennington <hp@redhat.com> 1:2.2.2-1
- 2.2.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-8
- change the volume applet size fix patch to work

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Sat Feb 22 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-6
- clamp size of volume applet to 24

* Thu Feb 20 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-5
- rebuild with datadir/wireless-applet and datadir/gen_util, 
  someone got overzealous deleting unpackaged files instead 
  of packaging them. #82279

* Fri Feb 14 2003 Jonathan Blandford <jrb@redhat.com> 1:2.2.0-4
- rebuild to get new gnome-panel

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-3
- nuke buildreq Xft

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com> 1:2.2.0-2
- fix path in modemlights patch

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 1:2.2.0-1
- 2.2.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 23 2002 Jeremy Katz <katzj@redhat.com> 1:2.1.3-1
- update to 2.1.3

* Tue Dec  3 2002 Havoc Pennington <hp@redhat.com>
- require newer panel, libgtop2
- require newer libgnomeui, libbonoboui

* Mon Dec  2 2002 Tim Powers <timp@redhat.com> 1:2.1.1-2
- remove unpackaged files from the buildroot

* Mon Dec  2 2002 Tim Powers <timp@redhat.com> 1:2.1.1-1
- update to 2.1.1
- add x86_64 to no_apm_archs

* Tue Aug 27 2002 Owen Taylor <otaylor@redhat.com>
- Register the cd player per-device (#72645).

* Fri Aug 23 2002 Owen Taylor <otaylor@redhat.com>
- Keep the CD device closed except when actually accessing it
  (bugzilla.gnome.org 91512)
- Register CD player so we can start only one CD player
  for display from magicdev. (#39208)

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- add ppc ppc64 to no_apm_arches #67564

* Wed Jul 31 2002 Nalin Dahyabhai <nalin@redhat.com>
- include applets in libexecdir

* Mon Jul 29 2002 Havoc Pennington <hp@redhat.com>
- 2.0.1, and build with new gail
- 69971 (use correct ppp on/off commands)
- remove scrollkeeper dtd-compliance patch, 
  fixed upstream apparently (patch doesn't apply anymore)

* Wed Jun 26 2002 Owen Taylor <otaylor@redhat.com>
- Fix %%find_lang

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild with new libs
- remove temporary hack for too-old libgnomeui
- add /etc/sound stuff to file list

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in different environment

* Thu Jun 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- fix a scrollkeeper validation bug

* Wed Jun 12 2002 Havoc Pennington <hp@redhat.com>
- remove panel-menu.schemas from the list of schemas.
- 2.0.0

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 1.105.0

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.103.0

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.100.0

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- GNOME 2 version

* Mon Apr 15 2002 Havoc Pennington <hp@redhat.com>
- merge translations

* Thu Apr 11 2002 Havoc Pennington <hp@redhat.com>
- default battstat applet to vertical mode

* Thu Mar 21 2002 Havoc Pennington <hp@redhat.com>
- add patch to adapt to yahoo web site changes, #61561

* Tue Mar  5 2002 Havoc Pennington <hp@redhat.com>
- remove requires libghttp4

* Mon Mar  4 2002 Havoc Pennington <hp@redhat.com>
- no apm on sparc, #60538
- obsolete battstat_applet for Ximian compat, #51427
- use ifup/ifdown ppp0 instead of pppon/pppoff for default 
  ppp command in modemlights, #54199

* Tue Feb 12 2002 Havoc Pennington <hp@redhat.com>
- 1.4.0.5, cross fingers
- add gconf-devel buildreq, though this is dubious as hell
  (pulled in by gtik using gnome-vfs, but if gtik actually
   accessed gconf it would fail due to gnorba conflict)
- patch totally busted charpick Makefile.am cflags override

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- automake14

* Thu Aug 30 2001 Alex Larsson <alexl@redhat.com>
- Removed annoying broken battery full dialog #52861
- Also fix mixer applet for USB sound #52603

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Wed Aug 15 2001 Alexander Larsson <alexl@redhat.com>
- Own /usr/share/gnome/gkb and /usr/share/gnome/help/*

* Wed Jul 18 2001 Havoc Pennington <hp@redhat.com>
- add some build requires
- remove ifarch build requires, replace with check in setup

* Wed Jul 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- sanitize specfile to RH style
- do not require apmd for s390 s390x

* Mon Jul  9 2001 Jonathan Blandford <jrb@redhat.com>
- new version

* Sun Jul 08 2001 Havoc Pennington <hp@redhat.com>
- remove extra .desktop file for battstat

* Sat Jul 07 2001 Havoc Pennington <hp@redhat.com>
- add battstat applet
- rearrange .desktop files for applets

* Tue Jun 12 2001 Than Ngo <than@redhat.com>
- fix isdn stuff to build against kernel-2.4.x
- use %%{_tmppath}

* Mon Jun 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- allow newer gettext versions

* Thu Mar 15 2001 Havoc Pennington <hp@redhat.com>
- translations

* Mon Feb 12 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese translation (ja.po, .desktop).
  Note: Please remove Source[23]: when release the next upstream version.

* Fri Jan 19 2001 Havoc Pennington <hp@redhat.com>
- 1.2.4

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Update Epoch

* Wed Jul 19 2000 Jonathan Blandford <jrb@redhat.com>
- Change slashapp to gnome-news app.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com
- %%defattr fixes
- Remove Docdir:

* Thu Jun 15 2000 Havoc Pennington <hp@redhat.com>
- 1.2.1
- use %%makeinstall
