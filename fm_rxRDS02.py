#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Fm Rxrds02
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class fm_rxRDS02(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Rxrds02", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Rxrds02")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fm_rxRDS02")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sampRate = sampRate = 19000
        self.inputSampRate = inputSampRate = 960000
        self.BPSKconst = BPSKconst = digital.constellation_bpsk().base()
        self.BPSKconst.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            16,
            firdes.root_raised_cosine(
                1,
                sampRate,
                1187.5,
                0.35,
                8))
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccf(
                interpolation=(int(sampRate/1000)),
                decimation=(int(inputSampRate/1000)),
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            500, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.low_pass_filter_1 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                20,
                inputSampRate,
                7000,
                700,
                window.WIN_HAMMING,
                6.76))
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(.01, 2, False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(BPSKconst)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, inputSampRate, True, 0 if "auto" == "auto" else max( int(float(0.1) * inputSampRate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'gqrx_20250520_173802_101100000_960000_fc.raw', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'outputRDS1.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(
            1,
            firdes.complex_band_pass(
                1000000,
                inputSampRate,
                (-57500),
                (-56500),
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccc(
            1,
            firdes.complex_band_pass(
                1,
                inputSampRate,
                (-19500),
                (-18500),
                100,
                window.WIN_HAMMING,
                6.76))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_1, 2))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_null_source_1, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.blocks_throttle2_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_const_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_rxRDS02")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sampRate(self):
        return self.sampRate

    def set_sampRate(self, sampRate):
        self.sampRate = sampRate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sampRate, 1187.5, 0.35, 8))

    def get_inputSampRate(self):
        return self.inputSampRate

    def set_inputSampRate(self, inputSampRate):
        self.inputSampRate = inputSampRate
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.inputSampRate, (-19500), (-18500), 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1000000, self.inputSampRate, (-57500), (-56500), 100, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.inputSampRate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(20, self.inputSampRate, 7000, 700, window.WIN_HAMMING, 6.76))

    def get_BPSKconst(self):
        return self.BPSKconst

    def set_BPSKconst(self, BPSKconst):
        self.BPSKconst = BPSKconst
        self.digital_constellation_decoder_cb_0.set_constellation(self.BPSKconst)




def main(top_block_cls=fm_rxRDS02, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
