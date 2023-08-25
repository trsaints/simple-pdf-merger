import tkinter as tk

def render_gui(gui):
	gui.origin_button.grid(
		row = 0,
		column = 2,
		columnspan = 3,
		padx = 12,
		pady = 8,
		ipadx = 8,
		sticky = tk.E+tk.W
	)
	gui.destination_button.grid(
		row = 1,
		column = 2,
		columnspan = 3,
		padx = 12,
		pady = 8,
		ipadx = 8,
		sticky = tk.E+tk.W
	)
	gui.merge_button.grid(
		row = 2,
		column = 0,
		columnspan = 3,
		padx = 12,
		pady = 8,
		sticky = tk.E+tk.W
	)
	gui.origin_display.grid(
		row = 0,
		column = 1,
		padx = 12,
		pady = 8
	)
	gui.destination_display.grid(
		row = 1,
		column = 1,
		padx = 12,
		pady = 8
	)
	gui.origin_label_frame.grid(
		row = 0,
		column = 1,
		padx = 12,
		pady = 8,
		sticky = tk.NW
	)
	gui.destination_label_frame.grid(
		row = 1,
		column = 1,
		padx = 12,
		pady = 8,
		sticky = tk.NW
	)
	gui.grid(sticky = tk.N+tk.E+tk.S+tk.W)

def update_display_output(display, output):
	display.configure(state = "normal")
	display.delete("1.00", "end")
	display.insert("end", output)
	display.configure(state = "disabled")
