# WP-001 — finite-prime Weil blocks cannot be independent positive Prime-Circle ray energies

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the natural route that identifies each finite-prime contribution to the Weil quadratic form with an independent positive semidefinite form on the Prime-Circle exponent ray. This does **not** rule out a global quotient, compression, supertrace, cohomological pairing, or other mechanism in which the finite places become positive only after coupling to the archimedean/pole sector.

## 1. Claim

Prime Circle already reproduces the exact finite-place coefficient profile

\[
(\log p)p^{-k/2},\qquad k\ge 1,
\]

through normalized cyclotomic resultants. PC-005 then completes this off-diagonal profile to the positive Poisson Toeplitz kernel

\[
K_p(a,b)=(\log p)p^{-|a-b|/2},\qquad a,b\ge1.
\]

However, the finite-prime contribution of the standard Weil quadratic form has the same prime-power coefficients with the **subtractive sign** and has **no `k=0` diagonal term**. On the exponent ray its coefficient matrix is therefore

\[
\boxed{
A_p=(\log p)I-K_p,
}
\]

i.e.

\[
A_p(a,a)=0,
\qquad
A_p(a,b)=-(\log p)p^{-|a-b|/2}\quad(a\ne b).
\]

Every such nonzero Hermitian zero-diagonal block is indefinite. Already the adjacent two-level principal block is

\[
\begin{pmatrix}
0&-(\log p)p^{-1/2}\\
-(\log p)p^{-1/2}&0
\end{pmatrix},
\]

with eigenvalues

\[
\pm (\log p)p^{-1/2}.
\]

Hence the exact Prime-Circle local kernel cannot simultaneously be

1. the finite-prime Weil summand coefficient-for-coefficient, and
2. an independently nonnegative local energy.

The missing positivity cannot be obtained by simply summing the already-positive PC-005 kernels over primes. A successful Mathia mechanism must instead explain why the **globally assembled** finite-prime, archimedean, and pole/counterterm pieces form a positive object after a canonical global operation.

## 2. Exact coefficient comparison

Let

\[
q=p^{-1/2},\qquad L=\log p.
\]

PC-004 proves for the prime-power cyclotomic ray that the normalized mutual interaction at separation `k>=1` is

\[
J^{(p)}_{a,a+k}=Lq^k.
\]

PC-005 adds the scale-difference self term `L` and obtains

\[
K_p(a,b)=Lq^{|a-b|},
\]

which is positive definite because its Fourier symbol is the Poisson kernel

\[
L\frac{1-q^2}{1-2q\cos\theta+q^2}>0.
\]

Now take the standard autocorrelation form of the Riemann-Weil explicit formula. If `f` is a real compactly supported logarithmic test and

\[
g=f*\widetilde f,
\]

then the finite-prime part of the Weil quadratic functional is, in the usual normalization,

\[
\boxed{
-2\sum_p\sum_{k\ge1}
(\log p)p^{-k/2}g(k\log p).
}
\tag{1}
\]

(The pole and archimedean terms are separate. Moving the entire explicit formula to the opposite side changes all signs simultaneously and does not alter the relative obstruction below.)

To compare (1) directly with the Prime-Circle exponent ray, let a finitely supported ray vector `c=(c_a)` have autocorrelations

\[
G_k(c)=\sum_{a\ge1}c_{a+k}\overline{c_a}.
\]

The coefficient-for-coefficient local ray realization of (1) is

\[
\mathcal A_p(c)
=-2L\sum_{k\ge1}q^k\operatorname{Re}G_k(c)
=\langle c,A_pc\rangle,
\]

where

\[
A_p=LI-K_p.
\]

Thus the positive completion discovered in PC-005 is not the desired Weil local form. Rather, the desired finite-place block is obtained by **removing exactly the positive diagonal that made the Poisson matrix positive and reversing its off-diagonal contribution relative to the positive energy**.

## 3. Zero-diagonal positivity obstruction

There is a basis-free elementary obstruction behind the two-by-two example.

If a Hermitian matrix `H` is positive semidefinite, Cauchy-Schwarz for the associated semidefinite form gives

\[
|H_{ab}|^2\le H_{aa}H_{bb}.
\]

Therefore

\[
H_{aa}=0\quad\Longrightarrow\quad H_{ab}=0
\quad\text{for every }b.
\]

Consequently a positive semidefinite Hermitian form with zero diagonal in every exponent-ray basis vector must be identically zero. Since the Weil finite-place coefficient block has nonzero prime-power off-diagonal entries, it cannot itself be a positive semidefinite local Gram form on that ray.

This is stronger than observing one negative eigenvalue numerically: it rules out the whole **termwise local-Gram interpretation** before any asymptotic or regularization issue is considered.

## 4. Why the PC-005 diagonal cannot simply be retained

One might try to keep

\[
K_p= L I + \text{off-diagonal terms}
\]

as the positive local geometry and declare the diagonal to be a harmless renormalization. That changes the target functional.

The prime-power side of the explicit formula starts at `k=1`; there is no finite-place `k=0` term `L g(0)` to absorb the diagonal. For a common ray norm the additional term would be

\[
(\log p)\|c\|^2
\]

at each prime. Summed without a cutoff, these self terms diverge as

\[
\sum_p\log p.
\]

With compact support only finitely many prime powers enter (1), but retaining a support-dependent diagonal still adds a new term not present in the Weil functional. Removing it later by hand merely returns to the indefinite matrix `A_p`.

So the PC-005 positive diagonal is mathematically meaningful as a local Poisson/GCD completion, but it is **not** an independently available positive contribution of the global Weil form.

## 5. Adversarial checks

### Sign convention

The obstruction is not an artifact of putting the explicit formula on one side or the other. In the convention where the zero-side Weil form is nonnegative under RH, the finite-prime term is subtractive relative to the archimedean/pole part, as in (1). Multiplying the whole identity by `-1` also reverses the target positivity inequality. What cannot be done is flip only the local prime sign while preserving the same global positivity target.

### Pole-neutral test constraints

The two-coordinate vectors used above are not claimed to parameterize every admissible continuous Weil test independently. Global test-function constraints can restrict the allowed subspace, and the archimedean/pole contribution can compensate the local negative directions. That is not a loophole in the stated result; it is exactly the conclusion:

\[
\boxed{
\text{positivity, if geometric, must be a property of a globally coupled object, not of each finite-place ray block.}
}
\]

The finding therefore rules out a **direct local-sum proof**, not semilocal/global positivity on a constrained space.

### Alternative positive completion

Adding a larger diagonal can make many Toeplitz matrices positive, but any such diagonal changes the explicit-formula functional unless the same intrinsic global construction produces and cancels it elsewhere. An arbitrary regularization or support-dependent subtraction fails the branch's canonicity gate.

### Matched controls

The matrix obstruction depends only on the exact coefficient/sign/diagonal structure, not on statistical peculiarities of the prime sequence. Replacing the cyclotomic derivation by any control that produces the same `Lq^k` ray coefficients leaves the obstruction unchanged. Therefore the positive Poisson completion by itself cannot be the arithmetic selector.

## 6. Relation to earlier Mathia evidence

This sharpens, rather than contradicts, the Prime-Circle sequence:

- [`PC-004`](../../prime_circle/findings/PC-004-normalized-resultants-weil-local-kernels.md) derives the exact finite-place off-diagonal coefficient `Lq^k`.
- [`PC-005`](../../prime_circle/findings/PC-005-discriminant-renormalization-completes-prime-ray-kernel.md) obtains the positive Poisson completion by adding the diagonal `L` from a separate scale difference.
- [`PC-006`](../../prime_circle/findings/PC-006-critical-gcd-kernel-and-potential-theory-downgrade-PC005.md) shows that the mutual and self pieces are not one intrinsic Dirichlet Gram energy and identifies the resulting kernel with classical GCD/Poisson potential theory.

WP-001 adds the global Weil-sign audit: even if one accepts the PC-005 completion as canonical local geometry, the coefficient matrix that actually matches the finite-prime Weil summand is `LI-K_p`, which is necessarily indefinite.

So the branch should no longer spend effort trying to prove RH by showing that **each PC prime ray is already a positive Weil place**. The local positivity is on the wrong completed object.

## 7. Prior art and novelty assessment

No general theorem of new mathematics is claimed here.

The underlying ingredients are classical:

- Weil's explicit formula supplies the subtractive prime-power term and the absence of a finite-place `k=0` summand.
- The elementary zero-diagonal PSD lemma is standard linear algebra.
- Burnol's `p`-adic scattering model is particularly close prior art: its time-delay spectral function is nonnegative, while the local Weil explicit formula appears only after an odd/even grading as a **supertrace**, already warning that local Weil data need not be an ordinary positive trace.
- Connes-Consani's archimedean work obtains positivity from a **compression** of the scaling action, and the semilocal adele-class program assembles places before asking for Weil positivity.
- The function-field analogy likewise points to a global intersection/cohomological sign mechanism rather than independent positive Euler-factor energies.

The durable contribution is therefore a **Mathia-specific impossibility principle**: the exact Prime-Circle kernel that looked most promising for a local Weil positivity proof cannot have the required sign and diagonal structure as an independent positive summand.

This redirects the search toward structures with a genuinely global operation—projection away from trivial directions, quotient/cohomology, signed/supertrace pairing, Schur complement/compression, intersection form, or an equally canonical coupling—that produces the archimedean and finite-prime terms together.

## 8. Decisive audit / falsification criterion

WP-001 would be falsified only by a construction that satisfies all of the following simultaneously:

1. derives from Prime Circle (or a directly identified Mathia-native replacement) without inserting the Weil kernel by definition;
2. yields the finite-place coefficients `-(log p)p^{-k/2}` for every `k>=1` with the audited Weil normalization;
3. has no extra uncancelled finite-place `k=0` term;
4. is independently positive for each prime place on the claimed local Hilbert space.

For an ordinary Hermitian Gram form on the exponent-ray basis, conditions 2–4 are incompatible by the zero-diagonal lemma. Any surviving proposal must therefore explain which hypothesis is genuinely changed by a **global** construction rather than hidden by notation or regularization.

## 9. Consequence for the research line

The main positive clue from Prime Circle survives only as **coefficient matching**, not as a local positivity mechanism.

The next viable gate is sharper:

\[
\boxed{
\text{Find one intrinsic global Mathia object whose positive/negative geometric theorem}
\\
\text{produces the finite-prime indefinite blocks and the archimedean/pole completion together.}
}
\]

A direct sum of independently positive prime-ray energies is now ruled out.