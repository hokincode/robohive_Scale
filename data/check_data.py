import h5py

# Replace <Path to h5 data> with the actual path to your HDF5 file
filename = 'baking_sample_data.h5'

# Open the HDF5 file in read mode
h5 = h5py.File(filename, 'r')

# List all trials available in the file
trials = list(h5.keys())
print("Trials available:", trials)

# Loop through each trial and display its contents
for trial in trials:
    print(f"\nContents of {trial}:")
    trial_data = h5[trial]

    # List all keys within the current trial
    trial_keys = list(trial_data.keys())
    print("Keys:", trial_keys)

    # If 'data' key exists, extract and display its contents
    if 'data' in trial_data:
        data = trial_data['data']
        data_keys = list(data.keys())
        print("Data keys:", data_keys)

        # Loop through each data key and display the associated data
        for data_key in data_keys:
            data_value = data[data_key][()]
            print(f"Data for {data_key}:", data_value)

    # If 'derived' key exists, extract and display its contents
    if 'derived' in trial_data:
        derived = trial_data['derived']
        derived_keys = list(derived.keys())
        print("Derived keys:", derived_keys)

        for derived_key in derived_keys:
            derived_value = derived[derived_key][()]
            print(f"Derived data for {derived_key}:", derived_value)

    # If 'config' key exists, extract and display its contents
    if 'config' in trial_data:
        config = trial_data['config']
        config_keys = list(config.keys())
        print("Config keys:", config_keys)

        for config_key in config_keys:
            config_value = config[config_key][()]
            print(f"Config data for {config_key}:", config_value)

# Close the HDF5 file
h5.close()
