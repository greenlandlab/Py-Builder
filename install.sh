mv py-builder /opt
mv pybuilder.service /etc/systemd/system
chcon -t systemd_unit_file_t /etc/systemd/system/pybuilder.service
systemctl daemon-reload
systemctl verify pybuilder.service
systemctl enable pybuilder.service
echo "Finished now please reboot your system incase"