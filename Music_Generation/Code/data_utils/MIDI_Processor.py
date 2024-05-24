import TMIDIX
import tqdm
import random
def MIDI_to_int(melody_chords_f):
    SEQ_LEN = 8192
    PAD_IDX = 835

    print('=' * 70)

    train_data = []

    for m in tqdm.tqdm(melody_chords_f):
      for mm in m:

        cscore = TMIDIX.chordify_score(mm)

        dat = [834]

        first_chord = True

        for chord in cscore:

          tones_chord = sorted(set([c[3] % 12 for c in chord]))

          try:
              chord_token = TMIDIX.ALL_CHORDS_SORTED.index(tones_chord) + 512
          except:
              checked_tones_chord = TMIDIX.check_and_fix_tones_chord(tones_chord)
              chord_token = TMIDIX.ALL_CHORDS_SORTED.index(checked_tones_chord) + 512

          dat.append(chord_token)

          if first_chord:
            dat.append(0)
            first_chord = False

          for c in chord:

                if c[2] == 0:
                    cha = 0
                if c[2] == 3:
                    cha = 1

                if c[0] != 0:
                  dat.extend([c[0], c[1]+128, ((cha * 128) + c[3])+256])
                else:
                  dat.extend([c[1]+128, ((cha * 128) + c[3])+256])

        dat = dat[:SEQ_LEN+1]
        dat += [PAD_IDX] * (SEQ_LEN+1 - len(dat))

        train_data.append(dat)

    random.shuffle(train_data)