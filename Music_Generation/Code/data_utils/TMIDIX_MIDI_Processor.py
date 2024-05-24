import os
import TMIDIX
import copy
def TMIDIX_MIDI_Processor(midi_file):

    melody_chords = []

    try:

        fn = os.path.basename(midi_file)

        #=======================================================
        # START PROCESSING

        raw_score = TMIDIX.midi2single_track_ms_score(midi_file)

        escore_notes = TMIDIX.advanced_score_processor(raw_score, return_enhanced_score_notes=True)[0]

        escore_notes = TMIDIX.augment_enhanced_score_notes(escore_notes, timings_divider=16)

        all_scores = []

        for ta in range(0, 6, 2):
          for pa in range(-1, 2):

            escore_notes_aug = copy.deepcopy(escore_notes)

            for e in escore_notes_aug:
              e[1] += ta
              e[2] += ta
              e[4] += pa

            violin_dscore = [d for d in escore_notes_aug if d[6] == 40]
            violin_mono_melody_score = [n[0] for n in TMIDIX.chordify_score([1000, violin_dscore])]

            piano_dscore = [d for d in escore_notes_aug if d[6] == 0]

            violin_piano_score_notes = sorted(violin_mono_melody_score+piano_dscore, key=lambda x: x[1])

            violin_piano_dscore_notes = [d[1:] for d in TMIDIX.delta_score_notes(violin_piano_score_notes,
                                                                                even_timings=True,
                                                                                compress_timings=True)]

            all_scores.append(violin_piano_dscore_notes)

        return all_scores

    except Exception as e:
      print('Error!')
      print('Exception', e)
      return None