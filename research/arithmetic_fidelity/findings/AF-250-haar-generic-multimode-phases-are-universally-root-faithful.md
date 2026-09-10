# AF-250 — Haar-generic multimode phases are universally root-faithful

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `OUTPUT-SAMPLING`, `GENERIC-PHASE-BOUNDARY`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-249 gives an exact all-sampling criterion for one conjugate Li pair but leaves the genuinely harder case in which several conjugate pairs share the dominant Keiper modulus. In that multimode setting, exponentially destructive cancellation is possible for specially chosen transcendental phases, but it is **Haar exceptional**.

Let

\[
P(x)=\sum_{\ell=1}^{M} c_\ell e^{2\pi i\langle k_\ell,x\rangle},
\qquad x\in\mathbb T^d,
\tag{1}
\]

be a nonzero trigonometric polynomial with distinct `k_\ell\in\mathbb Z^d`, nonzero coefficients `c_\ell\in\mathbb C`, and `M\ge2`. For `\alpha\in\mathbb T^d`, define

\[
F_\alpha(n)=P(n\alpha).
\tag{2}
\]

Then for Haar-almost every `\alpha` one has the full-sequence limit

\[
\boxed{
\lim_{n\to\infty}|F_\alpha(n)|^{1/n}=1.
}
\tag{3}
\]

Consequently, for Haar-almost every `\alpha`, **every** unbounded retained set `S\subset\mathbb N` satisfies

\[
\boxed{
\lim_{\substack{n\to\infty\\n\in S}}|F_\alpha(n)|^{1/n}=1.
}
\tag{4}
\]

So generic multimode phase families need no output-density, thickness, periodic-completeness, or recurrence condition at all: once the phase vector itself is outside an exponentially shrinking exceptional set, arbitrary unbounded sampling preserves the finite-mode root rate.

More quantitatively, there are constants `C_P>0` and `\gamma_P>0` such that for every `\varepsilon>0` and `N\ge1`,

\[
\mu\!\left\{\alpha:\exists n\ge N,
\ |P(n\alpha)|<e^{-\varepsilon n}\right\}
\le
\frac{C_P e^{-\gamma_P\varepsilon N}}
{1-e^{-\gamma_P\varepsilon}}.
\tag{5}
\]

For a trigonometric polynomial with exactly `M` frequencies, Wayne Lawton's small-value estimate allows one to take `\gamma_P=1/(M-1)` up to the fixed coefficient-dependent constant in `(5)`.

There is also a simultaneous countable-family form. If `\mathcal P` is any countable family of nonzero trigonometric polynomials on the same torus, then for Haar-almost every `\alpha`, `(3)` holds for **every** `P\in\mathcal P` at once.

In particular, fix `d` and consider all Li-shaped conjugate dominant modes

\[
P_m(x)=-2\sum_{j=1}^d m_j\cos(2\pi x_j),
\qquad m=(m_1,\ldots,m_d)\in\mathbb N^d.
\tag{6}
\]

Because the multiplicity family is countable, Haar-almost every phase vector `\alpha\in\mathbb T^d` is simultaneously all-sampling root-faithful for every positive integer multiplicity pattern `m`.

Thus the AF-248/AF-249 pathology is not merely extreme in the one-pair irrationality-base sense. In every fixed finite multimode dimension, failure of all-sampling Li root fidelity lies in a Haar-null phase set. This is a genericity theorem only; it does **not** show that phase vectors arising from actual Riemann zeros avoid that exceptional set.

## Why it matters

AF-246 identifies finite-mode root-rate loss with exponential approach to a trigonometric zero locus. AF-248 proves that elementary Li symmetries do not prevent such approach, and AF-249 shows that one conjugate pair is safe whenever its phase has no exponential rational-approximation defect. The remaining concern was that several co-dominant pairs might introduce a qualitatively worse simultaneous-cancellation mechanism for which coordinatewise Diophantine information is insufficient.

AF-250 separates **structural possibility** from **generic behavior**. Multimode cancellation can indeed be exponentially destructive, but for any fixed finite trigonometric mode it requires a Haar-exceptional phase generator. The proof does not need independence or mixing of the orbit `n\alpha`: multiplication by `n` preserves Haar measure, while a fixed nonzero trigonometric polynomial has only polynomially much Haar mass near zero. Exponentially shrinking amplitude thresholds are therefore summable, and the first Borel--Cantelli lemma removes them almost surely.

This materially changes the source-side interpretation of the current obstruction. The open issue is no longer whether multimode geometry generically creates hidden exponential cancellation. It does not. The hard arithmetic question is whether the **specific** Keiper phase vectors forced by possible off-critical Riemann zeros can be proved nonexceptional by a source theorem rather than by a genericity heuristic.

## Derivation / evidence

### 1. Fixed trigonometric polynomials have polynomial small-value mass

Let `\mu` be normalized Haar measure on `\mathbb T^d`. For a nonzero trigonometric polynomial `P`, there exist `C_P>0` and `\gamma_P>0` such that

\[
\mu\{x\in\mathbb T^d:|P(x)|<u\}
\le C_Pu^{\gamma_P},
\qquad 0<u\le1.
\tag{7}
\]

This is classical small-value/Remez--Łojasiewicz behavior. In the exact finite-frequency form needed here it also follows from Lawton's theorem on small values of Bohr almost periodic functions with bounded spectrum.

To see the bridge, choose `\omega\in\mathbb R^d` whose coordinates are rationally independent over `\mathbb Q` strongly enough that the finitely many numbers `\langle k_\ell,\omega\rangle` are distinct. Then

\[
f(t)=P(t\omega)
=\sum_{\ell=1}^M c_\ell e^{2\pi i t\langle k_\ell,\omega\rangle}
\tag{8}
\]

is a one-variable trigonometric polynomial with `M` distinct frequencies. The Kronecker flow `t\mapsto t\omega` is uniquely ergodic on `\mathbb T^d`, so its mean small-value frequency agrees with Haar measure of the corresponding sublevel set. Lawton proves for an `M`-frequency trigonometric polynomial a bound of the form

\[
J_f(u)\le C_{M-1}H_f^{-1/(M-1)}u^{1/(M-1)},
\tag{9}
\]

where `H_f` is the largest coefficient modulus. This gives `(7)` with `\gamma_P=1/(M-1)` after absorbing fixed constants.

If `|P|` is constant, the small-value statement near zero is trivial. Otherwise the relevant level-set boundaries are real-analytic null sets, so the usual unique-ergodic passage from continuous test functions to the sublevel indicator causes no ambiguity.

### 2. Integer multiplication does not change Haar small-value mass

For every integer `n\ge1`, the map

\[
M_n:\mathbb T^d\to\mathbb T^d,
\qquad M_n(\alpha)=n\alpha,
\tag{10}
\]

is a surjective continuous group endomorphism and therefore preserves normalized Haar measure. Hence

\[
\mu\{\alpha:|P(n\alpha)|<u\}
=
\mu\{x:|P(x)|<u\}.
\tag{11}
\]

Fix `\varepsilon>0` and define

\[
E_n(\varepsilon)
=
\{\alpha:|P(n\alpha)|<e^{-\varepsilon n}\}.
\tag{12}
\]

Equations `(7)` and `(11)` give

\[
\mu(E_n(\varepsilon))
\le C_Pe^{-\gamma_P\varepsilon n}.
\tag{13}
\]

Summing `(13)` over `n\ge N` immediately yields `(5)` by the union bound. In particular,

\[
\sum_{n=1}^\infty\mu(E_n(\varepsilon))<\infty.
\tag{14}
\]

No decorrelation property of the events is required.

### 3. Borel--Cantelli kills every positive exponential defect generically

By the first Borel--Cantelli lemma, for fixed `\varepsilon>0`, Haar-almost every `\alpha` belongs to only finitely many `E_n(\varepsilon)`. Intersect over the countable set of positive rational `\varepsilon`. For almost every `\alpha`, therefore, for every `\varepsilon>0` there is `N_\varepsilon(\alpha)` such that

\[
|P(n\alpha)|\ge e^{-\varepsilon n}
\qquad(n\ge N_\varepsilon(\alpha)).
\tag{15}
\]

Because `P` is bounded on the compact torus,

\[
|P(n\alpha)|^{1/n}
\le \|P\|_\infty^{1/n}\longrightarrow1.
\tag{16}
\]

Equation `(15)` gives the matching lower bound `e^{-\varepsilon}` for every `\varepsilon>0`. This proves the full limit `(3)`.

The quantifier over output samplings then becomes free. Any unbounded `S` is merely a subsequence of a sequence already converging to one, so `(4)` follows for **all** unbounded `S` simultaneously. This is stronger than proving a root-rate limsup separately for each preselected sampling set.

### 4. Countably many admissible modes remain generically safe simultaneously

For each nonzero `P`, let `G_P\subset\mathbb T^d` be the full-Haar-measure set on which `(3)` holds. If `\mathcal P` is countable, then

\[
G_{\mathcal P}
=
\bigcap_{P\in\mathcal P}G_P
\tag{17}
\]

still has Haar measure one.

The Li multiplicity family `(6)` is countable for fixed `d`, so almost every `\alpha` is safe for all such modes at once. This countable-intersection step matters because the dominant zero multiplicities are not known in advance, whereas they are discrete data rather than an uncountable coefficient freedom.

The same argument applies to any countable coefficient/frequency class whose individual members are nonzero. It does not justify an uncountable universal quantifier over arbitrary coefficients chosen after seeing `\alpha`.

## Keiper--Li consequence

Suppose RH is false and that the nearest poles of the Keiper--Li generating function consist, after grouping conjugates, of `d` co-dominant phase pairs. AF-244 gives a decomposition of the form

\[
\lambda_n=q^nP_m(n\alpha)+r_n,
\qquad q>1,
\qquad
\limsup_{n\to\infty}|r_n|^{1/n}<q,
\tag{18}
\]

with a nonzero finite conjugate trigonometric mode `P_m` determined by the dominant phases and positive integer zero multiplicities.

For a Haar-generic phase vector, `(3)` is stronger than the AF-246 condition needed to preserve the separated dominant rate. Choose `0<\rho<1` with

\[
\limsup |r_n|^{1/n}<q\rho.
\tag{19}
\]

Then choose `\varepsilon>0` with `e^{-\varepsilon}>\rho`. Equation `(15)` gives eventually

\[
q^n|P_m(n\alpha)|\ge(qe^{-\varepsilon})^n,
\tag{20}
\]

while the remainder is exponentially smaller. Therefore

\[
\boxed{
\lim_{n\to\infty}|\lambda_n|^{1/n}=q>1.
}
\tag{21}
\]

and every unbounded retained set has the same restricted root-rate limit `q`.

Thus, conditional on an off-RH dominant phase vector lying in the Haar-generic set above, **no infinite output sparsification can hide the off-critical exponential scale once the selected Li coefficients have actually been formed**.

This does not solve the separate source-access problem: forming a large retained `\lambda_n` may still require deep cancellation-coherent arithmetic input. Nor does Haar genericity establish anything about the actual zero-derived phase vector.

## Prior-art audit

Wayne M. Lawton, **“Distribution of Small Values of Bohr Almost Periodic Functions with Bounded Spectrum,”** *Journal of Siberian Federal University. Mathematics & Physics* 12(5) (2019), 571--578, DOI `10.17516/1997-1397-2019-12-5-571-578`, arXiv:`1904.09373`, proves that every nonzero Bohr almost periodic function with bounded spectrum has polynomially small mean measure near zero. For a trigonometric polynomial with `M` frequencies, his Theorem 1 gives an exponent `1/(M-1)` and a coefficient-height-controlled constant. The same paper explicitly discusses Mahler measure and a classical RH-equivalent cyclotomic estimate. The small-value estimate used in `(7)` is therefore prior art, not a new Arithmetic Fidelity theorem.

The first Borel--Cantelli lemma and Haar invariance of the multiplication maps on a torus are classical. The general shrinking-target literature likewise studies exceptional recurrent visits to shrinking sets; Hill and Velani, **“The Shrinking Target Problem for Matrix Transformations of Tori,”** *Journal of the London Mathematical Society* 60 (1999), 381--398, DOI `10.1112/S0024610799007681`, is adjacent background already used in AF-246. Their dynamical setting is not the same parameter-space argument here, and no mixing theorem is needed for `(14)`.

A targeted search for the exact combination of finite Keiper--Li dominant modes, Lawton-type small-value estimates, Haar-generic phase vectors, arbitrary unbounded output sampling, and the Li root-rate discriminator did not locate a standard statement matching `(3)`--`(6)` or `(18)`--`(21)`. This is not an exhaustive novelty proof. The derived contribution is the narrow synthesis: polynomial small-value mass plus Haar-preserving multiplication makes exponential multimode cancellation a measure-zero phase pathology, and therefore makes every unbounded output sampling root-faithful for generic finite Li phase families.

## Boundaries

**Genericity is not arithmetic evidence.** The Riemann zeros determine one specific phase vector. A Haar-full statement cannot be substituted for a theorem that this vector, or every vector allowed by genuine zeta constraints, avoids the exceptional set.

**Fixed finite dominant family.** The argument applies after AF-244 has reduced an off-RH singularity to finitely many poles at the smallest Keiper modulus. It does not provide a uniform statement as the number of co-dominant modes grows without bound.

**Countable mode families only.** Simultaneous generic safety follows for countably many fixed trigonometric polynomials, including all positive-integer Li multiplicity patterns in a fixed dimension. It does not permit coefficients to be chosen adversarially from an uncountable family after the phase vector is known.

**Ambient Haar measure can hide lower-dimensional arithmetic constraints.** If genuine zeta identities force the phase vector onto a proper subtorus or another structured subset, one must rerun the small-value argument with the appropriate intrinsic measure and verify that the relevant trigonometric mode does not vanish identically there. Full-torus genericity alone says nothing on a Haar-null constrained locus.

**Output sampling is not source compression.** Equation `(21)` concerns retention of an already-formed Li root discriminator. It does not reduce the arithmetic depth or cancellation budget required to compute the sampled coefficients.

## Research consequence

The multimode output frontier is now sharply divided. There is no generic finite-dimensional cancellation obstruction: for almost every admissible phase vector, every unbounded output sampling is root-faithful. The remaining difficult case is the exceptional arithmetic locus containing the actual zero-derived phases, if any.

A source-specific next theorem should therefore not try to prove generic equidistribution again. It should identify a property genuinely forced by the zeta zero set that excludes exponential membership in the sublevel events

\[
|P_m(n\alpha)|<e^{-cn}
\tag{22}
\]

for every `c>0` and for the actual finite multiplicity mode. Useful candidates include a simultaneous exponential-approximation bound, a lower bound for the relevant zero-derived linear forms, or a proof that genuine zeta constraints place the phase vector on a structured locus where an intrinsic analogue of the small-value/Borel--Cantelli argument remains valid.

Until such a theorem exists, AF-250 should be used only as a calibration result: the observed obstruction is possible but non-generic, so any successful RH route must replace genericity by an arithmetic exclusion of the exceptional shrinking-target set.