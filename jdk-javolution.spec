Name     : jdk-javolution
Version  : 5.5.1
Release  : 4
URL      : https://repo1.maven.org/maven2/javolution/javolution/5.5.1/javolution-5.5.1.jar
Source0  : https://repo1.maven.org/maven2/javolution/javolution/5.5.1/javolution-5.5.1.jar
Source1  : https://repo1.maven.org/maven2/javolution/javolution/5.5.1/javolution-5.5.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-javolution-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-javolution package.
Group: Data

%description data
data components for the jdk-javolution package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/javolution.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/javolution.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/javolution.xml \
%{buildroot}/usr/share/maven-poms/javolution.pom \
%{buildroot}/usr/share/java/javolution.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/javolution.jar
/usr/share/maven-metadata/javolution.xml
/usr/share/maven-poms/javolution.pom
