import numpy as np
import mne
# Read the CSV file as a NumPy array
import os
import numpy
import mne
import matplotlib
#matplotlib.use('Qt5Agg')
import sklearn
files = os.listdir()[0:-4]
def getPlot(path):
    with open(path, "r") as f:
        data = f.read().split('\n')[1:-1]
    data = np.array([[i.split(';')[j] for j in range(len(i.split(';'))) if j in [2, 4, 10, 12]] for i in data]).T
    ch_names = ['AF3', 'T8', 'AF4', 'T7']  # TODO: finish this list
    info = mne.create_info(ch_names, sfreq=128, ch_types='eeg')
    raw = mne.io.RawArray(data, info)
    montage = mne.channels.make_standard_montage(kind='standard_1020', head_size=0.095)
    raw.set_montage(montage, match_case=True)
    raw.plot_psd(area_mode='range', average=False);
    raw.info['bads'] = ['AF3']
    raw.interpolate_bads(reset_bads=True, mode='accurate')

    raw.plot(block=True);
    eog_events = mne.preprocessing.find_eog_events(raw, ch_name='AF3')
    n_blinks = len(eog_events)
    onset = eog_events[:, 0] / raw.info['sfreq'] - 0.25
    duration = np.repeat(0.5, n_blinks)
    annot = mne.Annotations(onset, duration, ['bad blink'] * n_blinks, orig_time=raw.info['meas_date'])
    raw.set_annotations(annot)
    print(raw.annotations)
    raw.plot(block=True, events=eog_events);


    from mne.preprocessing import ICA, create_eog_epochs
    decim = 3
    reject = dict(eeg=40e-6)

    #raw.filter(1., None, fir_design='firwin');
    ica = ICA(n_components=3, method='fastica', random_state=1)
    ica.fit(raw, decim=3)

    print(ica)
    #ica.plot_components(ch_type='eeg');
    eog_average = create_eog_epochs(raw, ch_name='AF3', reject_by_annotation=False).average();
    eog_epochs = create_eog_epochs(raw, ch_name='AF3', reject_by_annotation=False);  # get single EOG trials
    eog_inds, scores = ica.find_bads_eog(eog_epochs, ch_name='AF3', threshold=2.0, l_freq=1, h_freq=10,
                                         reject_by_annotation=True);

    # In[10]:

    ica.plot_scores(scores, exclude=eog_inds);
    ica.plot_sources(eog_average);
getPlot('23_02_2021_20_34_15.txt')

