#start_gui
#open_project file_path/project_name.xpr
update_compile_order -fileset sources_1

#1. Run Synthesis
	reset_run synth_1
	launch_runs synth_1 -jobs 8
	wait_on_run synth_1
	puts "Synthesis Complete"

#2. Run Implementation
	launch_runs impl_1 -jobs 8
	wait_on_run impl_1
	puts "Implementation Complete"

#3. Generate Normal bitstream
	launch_runs impl_1 -to_step write_bitstream -jobs 8
	wait_on_run impl_1
	puts "Bitstream Complete"
	open_hw

#turn on the FPGA board
	connect_hw_server
	open_hw_target

#4. Generating Normal bitstream
	set_property PROGRAM.FILE {file_path/project_name.runs/impl_1/picorv32.bit} [get_hw_devices xc7a35t_0]
	set_property PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property FULL_PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	current_hw_device [get_hw_devices xc7a35t_0]
	refresh_hw_device [lindex [get_hw_devices xc7a35t_0] 0]
	create_hw_cfgmem -hw_device [get_hw_devices xc7a35t_0] -mem_dev [lindex [get_cfgmem_parts {s25fl032p-spi-x1_x2_x4}] 0]

#5. Programming the FPGA
	set_property PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property FULL_PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property PROGRAM.FILE {file_path/project_name.runs/impl_1/picorv32.bit} [get_hw_devices xc7a35t_0]
	program_hw_devices [get_hw_devices xc7a35t_0]
	refresh_hw_device [lindex [get_hw_devices xc7a35t_0] 0]

#6. Displaying ILA waveform screen
	display_hw_ila_data [ get_hw_ila_data hw_ila_data_1 -of_objects [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]]

#7. Setting resetn as trigger
	set_property TRIGGER_COMPARE_VALUE eq1'bX [get_hw_probes resetn -of_objects [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]]
	set_property TRIGGER_COMPARE_VALUE eq1'bR [get_hw_probes resetn -of_objects [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]]
	puts "Trigger set"

#8. Command to write ila_trig file
	run_hw_ila -force -file file_path/project_name /ila_trig.tas [get_hw_ilas hw_ila_1]
	save_wave_config {file_path/project_name.hw/hw_1/wave/hw_ila_data_1/hw_ila_data_1.wcfg}
	close_hw

#10. Open implemented design & apply ila_trig
	open_run impl_1

#11. Apply the trig_at_startup 
	apply_hw_ila_trigger ila_trig.tas

#12. Write trig_at_startup bitstream
	write_bitstream -force file_path/project_name /trig_at_startup.bit
	puts "Trigger at startup bitstream generated Successfully"
	open_hw

#do not turn off the board
	connect_hw_server
	open_hw_target

	set_property PROGRAM.FILE {file_path/project_name.runs/impl_1/picorv32.bit} [get_hw_devices xc7a35t_0]
	set_property PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property FULL_PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	current_hw_device [get_hw_devices xc7a35t_0]
	refresh_hw_device [lindex [get_hw_devices xc7a35t_0] 0]

	create_hw_cfgmem -hw_device [get_hw_devices xc7a35t_0] -mem_dev [lindex [get_cfgmem_parts {s25fl032p-spi-x1_x2_x4}] 0]
	display_hw_ila_data [ get_hw_ila_data hw_ila_data_1 -of_objects [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]]

#programming trig_at_startup bitstream
	set_property PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property FULL_PROBES.FILE {file_path/project_name.runs/impl_1/picorv32.ltx} [get_hw_devices xc7a35t_0]
	set_property PROGRAM.FILE {file_path/project_name /trig_at_startup.bit} [get_hw_devices xc7a35t_0]
	program_hw_devices [get_hw_devices xc7a35t_0]
	refresh_hw_device [lindex [get_hw_devices xc7a35t_0] 0]
	wait_on_hw_ila [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]
	display_hw_ila_data [upload_hw_ila_data [get_hw_ilas -of_objects [get_hw_devices xc7a35t_0] -filter {CELL_NAME=~"picorv_ila"}]]

#15. Export ILA data to csv
	write_hw_ila_data -csv_file {path_to_save_the_results\faulty.csv} hw_ila_data_1
	save_wave_config {file_path/project_name.hw/hw_1/wave/hw_ila_data_1/hw_ila_data_1.wcfg}
	close_hw
	close_design

#adding new faulty file and removing previous one
	add_files -norecurse path_where_all_faulty_verilogfiles_are_saved/fault2.v
	update_compile_order -fileset sources_1
	export_ip_user_files -of_objects  [get_files path_where_all_faulty_verilogfiles_are_saved /fault1.v] -no_script -reset -force -quiet
	remove_files path_where_all_faulty_verilogfiles_are_saved /fault1.v update_compile_order -fileset sources_1
