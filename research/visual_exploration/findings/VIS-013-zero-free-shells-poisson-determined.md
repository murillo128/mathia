# VIS-013 — zero-free nested log-modulus shells are Poisson-determined

## Claim

Let `xi` be Riemann's entire xi function, let `rho` be a zero of exact multiplicity `m>=1`, and remove the complete local zero monomial as in `VIS-012`:

`H_rho(w)=xi(rho+w)/(a_m w^m)`, with `H_rho(0)=1`.

Let

`R_rho = inf_{rho' != rho} |rho'-rho|`

where the infimum ranges over the remaining nontrivial zeros with multiplicity after the local copies of `rho` are removed. For `0<r<R_rho`, define the circular log-modulus shell

`u_r(theta)=log|H_rho(r e^{i theta})|`.

Then for every `0<r_1<r_2<R_rho`, the inner shell is exactly the Poisson extension of the outer shell:

`u_{r_1} = P_{r_1/r_2} * u_{r_2}`

on the circle, where `P_q` is the usual unit-disk Poisson kernel and convolution uses normalized angular measure.

Equivalently, with Fourier convention

`\hat u_r(n)=(1/(2 pi)) int_0^{2 pi} u_r(theta)e^{-i n theta} d theta`,

one has

`\hat u_r(0)=0`

and, for every integer `n`,

`\hat u_{r_1}(n)=(r_1/r_2)^{|n|} \hat u_{r_2}(n)`.

For `n>=2`, `VIS-012` identifies the positive-frequency coefficients explicitly as

`\hat u_r(n)=((-1)^(n-1) r^n/(2n)) sum_(rho' != rho) (rho-rho')^(-n)`.

Thus, before another zero enters the disk, a nested family of circular log-modulus portraits contains **no independent radial multiscale channel**: every inner view is a deterministic Abel-Poisson smoothing of any outer view, and each angular Fourier mode has the forced radial law `r^{|n|}`.

**Evidence/status:** `CLASSICAL-POISSON + EXACT-DERIVED + NEGATIVE/BASELINE`.

No novelty is claimed for Poisson harmonic extension, Jensen's mean-value consequence, or Fourier-mode scaling of a harmonic function. The durable Mathia consequence is the exact boundary this imposes on the accepted critical-strip multiscale clue.

## Exact derivation

Because `H_rho(0)=1` and `H_rho` has no zero in `|w|<R_rho`, every closed disk `|w|<=r_2<R_rho` admits a single-valued holomorphic logarithm

`L(w)=log H_rho(w)`

normalized by `L(0)=0`. Therefore

`U(w)=Re L(w)=log|H_rho(w)|`

is harmonic on that disk.

Apply the Poisson formula in the disk of radius `r_2`. For `w=r_1 e^{i theta}` with `q=r_1/r_2`,

`U(r_1 e^{i theta})
 = (1/(2 pi)) int_0^{2 pi}
   P_q(theta-phi) U(r_2 e^{i phi}) d phi`.

This is exactly the first claim.

The Poisson kernel has Fourier multipliers `q^{|n|}`. Taking angular Fourier coefficients gives

`\hat u_{r_1}(n)=q^{|n|}\hat u_{r_2}(n)`.

The zeroth coefficient is zero because the harmonic mean-value property gives

`\hat u_r(0)=U(0)=log|H_rho(0)|=0`.

For the explicit positive-frequency formula, write

`L(w)=sum_(n>=1) b_n w^n`.

Then

`u_r(theta)=Re sum_(n>=1) b_n r^n e^{i n theta}`,

so for `n>=1`

`\hat u_r(n)=(1/2)b_n r^n`.

For `n>=2`, `VIS-012` gives

`L^(n)(0)=(-1)^(n-1)(n-1)! sum_(rho' != rho)(rho-rho')^(-n)`,

hence

`b_n=L^(n)(0)/n!
     =((-1)^(n-1)/n) sum_(rho' != rho)(rho-rho')^(-n)`,

which yields the stated expression. The `n=1` mode obeys the same radial scaling but retains the genus-one linear/gauge dependence already excluded from the raw reciprocal-moment formula in `VIS-012`.

## Visual check

The retained artifact

`research/visual_exploration/visualizations/zero-free-shell-poisson-collapse.md`

evaluates `xi` around its first nontrivial zero at 60 decimal digits, removes the simple-zero monomial, samples `u_r(theta)` on 1024 equally spaced angles, and compares radii

`r in {0.75, 1.5, 2.5, 3.5}`.

The next critical-line zero is approximately `6.887314497` units away in the local `w` coordinate, so all four circles stay inside the same zero-free disk. For modes `n=2,...,8`, the curves `|\hat u_r(n)|/r^n` collapse; the maximum relative spread across the four radii is about `2.3e-10`, consistent with numerical evaluation and discrete Fourier error.

This finite computation is only an integrity check and visualization of the exact theorem. It is not the evidence for the claim.

## Research consequence

The accepted clue

`research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md`

had already removed the universal local monomial, exact critical-line reflection parity, and any fixed finite vector of reciprocal-power log jets. The present result removes a stronger apparent escape: **nested circular scale changes inside one zero-free neighborhood are themselves analytically forced**, even if the full shell uses infinitely many Fourier modes.

Consequently, a candidate cross-scale statistic should not be promoted merely because several nested circles have a coherent evolution. Before the nearest additional zero enters, that evolution is exactly the Poisson semigroup acting on one boundary profile.

A genuinely new finite-radius route must therefore exploit information not present in this zero-free radial transfer. Natural surviving possibilities include:

- radii that cross a zero-entry event, where `log|H_rho|` ceases to be harmonic on the full disk and Jensen/Poisson bookkeeping acquires explicit zero contributions;
- comparisons of outer-shell data across different central zeros or height windows after the Poisson scaling baseline is removed;
- non-circular domains or jointly moving neighborhoods whose change is not just harmonic inward continuation;
- a statistic tied to how several zeros enter, interact, or reorganize across spacing-scale boundaries rather than to smooth evolution inside one zero-free disk.

This does not prove that mesoscopic zeta geometry is classical or empty. It identifies the exact radius regime in which a visually compelling nested-shell effect cannot constitute independent multiscale evidence.

## Prior art and novelty assessment

The mathematical mechanism is standard complex analysis. The Poisson integral reconstructs a harmonic function inside a disk from its boundary values and multiplies angular Fourier mode `n` by the radial factor `q^{|n|}`; Jensen's formula reduces to the harmonic mean-value property for `log|f|` when `f` is zero-free. These facts are classical and are not claimed as Mathia discoveries.

`VIS-012` supplies the line-specific bridge from the Taylor/logarithmic coefficients of `H_rho` to reciprocal-power moments of the remaining xi-zero set. `VIS-013` combines that existing bridge with the classical Poisson semigroup to classify an entire family of nested visualizations as a forced analytic baseline.

A focused prior-art check found the Poisson/Abel-Poisson mechanism as standard harmonic/Fourier theory; no novelty claim is made for it. The only durable contribution here is the negative-control interpretation for the current visual research frontier.

## Boundary conditions and falsification

The theorem requires both radii to lie strictly below `R_rho`. Once another zero lies inside the outer circle, `log|H_rho|` is no longer harmonic on the whole disk and the simple zero-free Poisson relation does not apply without explicit Poisson-Jensen zero terms.

The statement concerns circular shells centered at the chosen zero. It does not say that every deformation of a neighborhood, every annular statistic, or every cross-zero comparison is Poisson-trivial.

The full outer shell may encode infinitely many zero moments. The theorem says that **changing only the radius inward adds no new independent information**; it does not say that a finite vector of moments reconstructs the outer shell.

The result is independent of RH. Reflection symmetry on the critical line adds the parity constraints from `VIS-011`, but the Poisson transfer itself requires only analyticity and zero-freeness after the local monomial is removed.
