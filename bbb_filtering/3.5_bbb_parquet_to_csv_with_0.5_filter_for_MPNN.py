import pandas as pd

# Load merged parquet file
merged_file = "merged_final_passed.parquet" # This has been relocated to a compressed folder.
df = pd.read_parquet(merged_file)

threshold = 0.998510  # 50% reduction to ~1 million molecules

# Filter molecules above the threshold
df_filtered = df[df["bbb_probability"] >= threshold]

# Save filtered dataset
output_filtered = "filtered_molecules_for_GCN.parquet" # This has been relocated to a compressed folder.
df_filtered.to_parquet(output_filtered)

print(f"\nFiltered dataset saved to {output_filtered}")
