# Mathia WI-011 finite formalization

This directory machine-checks the finite deduction layer controlled by
[`murillo128/mathia#74`](https://github.com/murillo128/mathia/issues/74).

- `WI011_GATE0.md` records the independently reviewed fresh statement, adversarial, prior-art,
  Mathlib-reuse, and dependency gate against current WI-011.
- `WI011TraceEnergy.lean` proves the scalar trace--energy envelope, pressure transfer, and exact
  `m = 438` branch/radical arithmetic.
- `WI011FourPointAssembly.lean` proves the four-point coefficient ledger, parameterized local
  certificate-to-block theorem, exact shifted-window and finite endpoint accounting, and the
  combined `wi011_m438_finite_splice` theorem.

Build with the repository toolchain:

```text
lake build MathiaFormalization
```

The source files print the axiom footprints of the principal theorems. The accepted footprint is
limited to `propext`, `Classical.choice`, and `Quot.sound`, the standard axioms reported by these
Mathlib-backed finite proofs.

## Attribution and integration boundary

The trace--energy envelope and window-in-frame accounting are prior art from
`tawanerguo-cn/zeta-simple-zeros`, independently rederived at historical revision
`0102fd8915c88fdd7c66231467745c17c0005fe4` of `trmdy/zeta-simple-zeros-673137`.
The local four-point certificate is the external Lean theorem `four_point_cert` in
`teal-sea/zeta-lab`; Mathia does not copy or reprove it here.

Accordingly, `wi011_m438_finite_splice` takes the local certificate as an explicit hypothesis.
Connecting this finite theorem to the external zeta stability/explicit-formula bridge requires a
compatible downstream integration. This project intentionally does not import the external
Lean `v4.33.0-rc2` path-dependent zeta graph. No theorem here claims the full asymptotic zeta
result, the decimal simple-zero proportion, or any statement about RH.

The earlier qwen-lean PR #105 is retained only as prior execution evidence. This Mathia project,
Gate, branch, and PR are the canonical delivery for issue #74.
