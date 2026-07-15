import { readdirSync } from "node:fs";
import path from "node:path";
import process from "node:process";

import { countPhysicalLines } from "./count-physical-lines.js";

const maxActiveSliceLines = 500;
const repositoryRoot = process.cwd();

function listActiveSliceDocuments(): string[] {
  const activeSliceDirectory = path.join(repositoryRoot, "docs/slices/active");

  return readdirSync(activeSliceDirectory, { withFileTypes: true })
    .filter(
      (entry) =>
        entry.isFile() &&
        entry.name.endsWith(".md") &&
        entry.name !== "README.md",
    )
    .map((entry) => path.join(activeSliceDirectory, entry.name));
}

const failures = listActiveSliceDocuments()
  .map((filePath) => ({
    filePath,
    lineCount: countPhysicalLines(filePath),
  }))
  .filter((file) => file.lineCount > maxActiveSliceLines)
  .map(
    (file) =>
      `${path.relative(repositoryRoot, file.filePath)} has ${String(file.lineCount)} lines; active slice documents must stay at or below ${String(maxActiveSliceLines)} lines.`,
  );

if (failures.length > 0) {
  console.error("Active slice length validation failed:");
  for (const failure of failures) {
    console.error(`- ${failure}`);
  }
  process.exitCode = 1;
} else {
  console.info("Active slice length validation passed.");
}
