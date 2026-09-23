# MC-476 — Sifted restriction is coefficient-blind at zero frequency

**Status:** `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The restriction theory for general sifted sets developed by Bera and Viswanadham applies directly to the **local pair-sieve geometry** in the rough×rough component of `MC-471`--`MC-475`, throughout its stated range `z <= H^(1/4)`. However, the resulting restriction estimate by itself cannot supply the missing conductor-power cancellation against the translated-ratio character phase

\[
K_h(n)=\chi(n+h)\overline{\chi(n)}.
\]

The reason is structural rather than numerical: the theorem is uniform in the coefficient sequence and sees it only through its `ell^2` mass. At the zero additive frequency it therefore cannot distinguish the oscillatory coefficients `K_h(n)` from constant positive coefficients supported on the same sifted set, except for at most two character zeros when `H<=p`.

More precisely, let `p` be the prime character conductor, let

\[
W_z=\prod_{\substack{q<z\\q\ne p}}q,
\qquad
A_{W_z,h}(n)=\mathbf 1_{(n(n+h),W_z)=1},
\tag{1}
\]

and let `I={M+1,...,M+H}`. For a surviving even shift `h` when `2|W_z`, translate `n=M+m`, `1<=m<=H`, and for every sieve prime `q` use the forbidden set

\[
\mathcal L_q(M,h)=\{-M,-M-h\}\pmod q.
\tag{2}
\]

Then

\[
|\mathcal L_q(M,h)|=
\begin{cases}
1,&q\mid h,\\
2,&q\nmid h,
\end{cases}
\tag{3}
\]

with the surviving `q=2` factor always in the first case. Thus the pair-sifted points of `I` are exactly the translate of the sifted set in Bera--Viswanadham's framework.

Their hypotheses hold uniformly: `(H1)` follows from `lambda(q)<=2<=2q^(1/4)`, and `(H2)` holds with sieve dimension `kappa=2`, since primes dividing `h` only reduce the local factor and

\[
\prod_{3\le q<y}\left(1-\frac2q\right)^{-1}
\asymp C\prod_{3\le q<y}\left(1-\frac1q\right)^{-2}
\ll (\log y)^2.
\tag{4}
\]

The ratio between the two products in `(4)` converges because its local logarithm is `O(q^{-2})`.

Let

\[
\mathcal S_{M,h}(H)=\{1\le m\le H:A_{W_z,h}(M+m)=1\},
\qquad
J=|\mathcal S_{M,h}(H)|.
\tag{5}
\]

Bera--Viswanadham Theorem 1.2, specialized to a singleton frequency set and any fixed `ell>2`, gives

\[
\left|\sum_{m\in\mathcal S_{M,h}(H)}a_m\right|
\le
C^{1/\ell}
\left(
\frac{H+1}{G(z)}
\sum_{m\in\mathcal S_{M,h}(H)}|a_m|^2
\right)^{1/2},
\tag{6}
\]

provided `z<=H^(1/4)`. Here `G(z)` is their sieve quantity and `C` depends only on the fixed restriction/sieve parameters.

Taking

\[
a_m=K_h(M+m)
\tag{7}
\]

there are at most two omitted unit-modulus terms when `H<=p`, so

\[
\sum_{m\in\mathcal S_{M,h}(H)}|a_m|^2=J+O(1).
\tag{8}
\]

But `(6)` contains **no further information about the phase of `a_m`**. Replacing `(7)` by `a_m=1` leaves the same norm input (up to `(8)`) while its zero-frequency sum is exactly `J`. Thus direct application of the restriction theorem cannot detect the translated-ratio cancellation that the live discrepancy requires.

The sieve factor cannot hide a conductor-power gain either. Bera--Viswanadham Lemma 2.4 gives

\[
G(z)\le V(z),
\tag{9}
\]

and `(4)` gives `V(z)<<log^2 z` for this pair sieve. Hence when `z` is at most a fixed power of `p`, the entire generic sieve gain available through `G(z)` is polylogarithmic, not `p^{-eta}`. Any power saving in the character conductor must therefore enter through an **additional coefficient-specific estimate** that uses the arithmetic of `K_h`, not through the restriction inequality alone.

This closes the standalone proposal

> pair-sieve restriction theorem + plug in `K_h` at zero frequency -> conductor-power cancellation.

It does **not** close sieve restriction as infrastructure. In particular, Bera--Viswanadham's proof uses an enveloping-sieve majorant with a rational Fourier expansion supported on denominators `q<=z^2`. Coupling such a compressed majorant to a `K_h`-specific character estimate before scalarization is genuinely different from both the full `W`-grid obstruction of `MC-475` and the coefficient-blind application `(6)`.

No estimate for the true incomplete discrepancy, no Möbius bound, no zero-free region and no RH consequence follow.

## 1. The shifted pair sieve is an instance of the general sifted-set theorem

Bera and Viswanadham allow an arbitrary forbidden subset `L_q` of each prime residue ring, subject to a cardinality bound and a sieve-dimension hypothesis. Translation of the interval does not change those cardinalities: condition `(1)` for `n=M+m` excludes exactly the two residues in `(2)`.

For odd `q`, the two residues coincide precisely when `q|h`. At `q=2`, an odd `h` forbids both residue classes and the rough×rough set is empty, exactly the parity degeneration already isolated in `MC-472`. Therefore only even `h` survives once `2|W_z`, and then the forbidden set at `2` has cardinality one and is proper.

For the growth hypothesis, if `q|h` the local factor `(1-1/q)^(-1)` is smaller than the generic `(1-2/q)^(-1)`. For odd `q`,

\[
\frac{(1-1/q)^2}{1-2/q}
=1+O(q^{-2}),
\tag{10}
\]

so the quotient of the product in `(4)` by the square of the Mertens product converges to a finite positive constant. This verifies the required `V(y)<<log^2 y` uniformly in `h`; removing the single conductor prime `p` only decreases the product by a bounded local modification.

Thus the modern sifted restriction theorem is not merely adjacent literature: its abstract local model contains the live pair sieve exactly in the range `z<=H^(1/4)`.

## 2. The zero-frequency specialization forgets the character phase

Theorem 1.2 controls an `ell^ell` norm over any separated frequency set. For a singleton frequency set `{0}`, the separation condition is vacuous; choosing separation parameter `delta=1` gives `(6)`.

The right-hand side depends on `(a_m)` only through

\[
\sum_{m\in\mathcal S}|a_m|^2.
\tag{11}
\]

For translated-ratio character coefficients this mass is the sifted occupancy up to at most two points. It is therefore essentially identical to the mass of the constant coefficient sequence on the same set.

This is the exact obstruction. Restriction theory gives strong information about how a sifted set distributes additive Fourier mass **uniformly over coefficient sequences**. The live Mathia problem needs the opposite kind of information at the distinguished zero mode: cancellation caused specifically by the multiplicative/rational phase `K_h`. A theorem whose input intentionally quotients away coefficient phase cannot create that information afterward.

The conclusion is narrower than saying restriction theory is useless. It says that a direct zero-mode use of a coefficient-uniform restriction inequality is the wrong endpoint object for the desired character cancellation.

## 3. The sieve dimension is only logarithmic at this stage

For the pair sieve, Bera--Viswanadham's quantity `V(z)` has dimension two. Combining their Lemma 2.4 with `(4)` gives

\[
G(z)\ll (\log z)^2.
\tag{12}
\]

Consequently, even before accounting for the actual occupancy `J`, the restriction normalization itself cannot contribute a fixed negative power of `p` when `z=p^{O(1)}`. Any such power must come from a theorem sensitive to the conductor-`p` character phase.

This also prevents a misleading interpretation of the `ell>2` improvement over Parseval. The endpoint failure at `ell=2` is real, and the restriction theorem is genuinely stronger than the plain full-grid Hilbert-space estimate closed by `MC-475`. But its strength is an additive-combinatorial statement about the sifted support; it is not automatically a mixed sieve/character estimate.

## 4. The enveloping sieve remains a concrete escape hatch

The same paper points to a more useful object than the black-box restriction inequality for this line. Its proof constructs an enveloping-sieve majorant `beta` and expands that majorant into rational additive frequencies with denominators

\[
q\le z^2.
\tag{13}
\]

This is qualitatively different from expanding the exact hard mask modulo the full primorial `W_z`, whose complete Fourier frame has dimension `W_z` and is fatal under plain `ell^2` coupling by `MC-475`.

However, positivity of the majorant is not enough for the signed character sum. From

\[
A_{W_z,h}(n)\le \beta(n)
\tag{14}
\]

one cannot infer

\[
\left|\sum K_h(n)A_{W_z,h}(n)\right|
\le
\left|\sum K_h(n)\beta(n)\right|.
\tag{15}
\]

A viable use of the enveloping sieve must therefore do one of two things: place the majorant inside a legitimate positive quadratic/restriction argument that still retains enough `K_h` information, or control the signed replacement error `sum K_h(A-beta)` on the actual source interval. The latter is exactly the approximation-cost side of the accepted source-frame clue.

This turns “try sieve restriction” into a much sharper question: **can the low-denominator enveloping representation be coupled to character-specific cancellation before its positive majorization or norm closure discards the phase?**

## 5. Prior art and novelty boundary

The source is Tanmoy Bera and G. K. Viswanadham, *Restriction estimates with sifted integers*, arXiv:2512.21640v3, revised 13 May 2026, DOI `10.48550/arXiv.2512.21640`. Their Theorems 1.1--1.4 establish restriction/large-sieve estimates for general sifted sets under `(H1)`--`(H2)`; Section 3 imports the Ramaré--Ruzsa enveloping sieve, and their proof explicitly uses a majorant rather than studying the sifted characteristic function directly.

Bera--Viswanadham generalize the Green--Tao Selberg-sieve restriction framework already cited in `MC-474`--`MC-475`. No novelty is claimed for their restriction theorem, the enveloping sieve, the dimension-two product estimate, or the observation that a coefficient-uniform norm bound cannot by itself distinguish two coefficient sequences with the same `ell^2` mass.

The line-specific contribution is the exact specialization of their hypotheses to the translated two-residue pair sieve and the resulting **method boundary**: the newest available general sifted restriction theorem does not by itself supply the missing character-conductor power saving at zero frequency, while its low-denominator enveloping representation identifies a narrower mixed sieve/character problem that is not covered by `MC-473`--`MC-475`.

## Boundaries and falsification tests

- **Range:** the cited restriction theorem is used only for `z<=H^(1/4)`. No conclusion is drawn from it outside that range.
- **Parity:** when `2|W_z`, odd `h` has no rough×rough survivors; the theorem specialization concerns the surviving even shifts.
- **No lower bound for the true sum:** coefficient-blindness diagnoses what the theorem can see. It does not prove that `sum K_h A` is large.
- **No obstruction to mixed estimates:** a theorem combining the enveloping sieve with conductor-sensitive character cancellation is not ruled out.
- **No majorant substitution by sign:** inequality `(14)` cannot be inserted directly into a signed sum; any such step must be justified through a positive form or an explicit error estimate.
- **Occupancy is separate:** an interval with exceptionally few sifted points is automatically easy, but that is support sparsity, not translated-ratio phase cancellation.
- **The `ell>2` theorem remains genuinely stronger than Parseval:** the present result closes only its standalone use as the missing zero-frequency character estimate.

## Consequence for the research line

The rough×rough route is now narrower again. `MC-473` rules out full divisor branching plus termwise completion, `MC-474` rules out exact hard-mask Fourier `ell^1` recombination, and `MC-475` rules out plain full-grid `ell^2` coupling. The present result shows that invoking modern general sifted restriction theory as a black box still does not expose the missing arithmetic phase: at zero frequency its bound is coefficient-uniform and its sieve normalization carries at most logarithmic-scale information.

The most concrete surviving restriction-style route is therefore no longer “prove a restriction estimate.” Such an estimate already exists for the local pair-sieve class. The live question is whether its **low-denominator enveloping-sieve representation** can be paired with a conductor-sensitive estimate for `K_h`, with the majorant/replacement error paid before phase information is lost. Bilinear or dispersion decompositions that avoid positive closure remain separate surviving routes.