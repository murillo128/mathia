# MC-057 — Exact-prefix quadratic interpolants already require quadratic conductor

**Status:** `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-CORRECTION`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `X>=2`. Let `q>X` be an odd prime and let

\[
\chi(n)=\left(\frac{n}{q}\right)
\]

be the primitive quadratic character modulo `q`. Assume the exact-prefix condition from `MC-055`:

\[
\chi(p)=-1
\qquad\text{for every prime }p\le X.
\tag{1}
\]

Let `ell(q)` denote the least prime quadratic residue modulo `q`. Then `(1)` gives

\[
\boxed{\ell(q)>X.}
\tag{2}
\]

Because `(2/q)=-1`, necessarily

\[
q\equiv3\ \text{or}\ 5\pmod 8.
\tag{3}
\]

Classical least-prime-residue theory then forces a **single-interpolant quadratic conductor floor**. For every `X>=677`, every prime-conductor quadratic character satisfying `(1)` obeys

\[
\boxed{q>3X^2.}
\tag{4}
\]

For the particular `q\equiv5 (mod 8)` construction used in `MC-055`, the stronger source theorem of Ramírez Viñas gives

\[
\boxed{q>4X^2+1.}
\tag{5}
\]

Thus the quadratic exact-prefix escape isolated in `MC-055` cannot use subquadratic prime conductors, even for a **single** moving comparator. In particular, the pairwise Burgess coherence bound of `MC-056`,

\[
q_1q_2\gg_\delta X^{4-\delta},
\]

is asymptotically dominated on this exact-prefix prime-quadratic family by the individual classical bounds: two such comparators already satisfy `q_1q_2>9X^4`, and two members of the specific `q_i\equiv5 (mod 8)` family satisfy `q_1q_2>16X^4` up to the harmless `+1` terms.

No bound for `M(X)` follows. The result is a prior-art correction to the moving-comparator complexity frontier: the relevant quadratic conductor cost is already visible one interpolant at a time.

## 1. Exact prefix agreement is exactly a least-prime-residue exclusion

Condition `(1)` says that every prime through `X` is a quadratic nonresidue modulo `q`. Since `q>X`, none of those primes is the conductor prime and no Legendre symbol vanishes. Therefore the least prime with `chi(p)=1` satisfies `(2)`.

This is stronger information than the square-free-supported coefficient agreement

\[
f_X(n)=\mu(n)^2\chi(n)=\mu(n)\qquad(n\le X)
\]

used in `MC-055`: it identifies a classical arithmetic invariant of the conductor itself. The exact-prefix construction is not merely a finite interpolation problem; it asks for a prime modulus whose **least prime quadratic residue lies beyond the observation scale**.

The value at `2` fixes the only possible congruence branches. The supplementary law

\[
\left(\frac2q\right)=(-1)^{(q^2-1)/8}
\]

combined with `chi(2)=-1` yields `(3)`.

## 2. The `q ≡ 3 (mod 8)` branch has a quadratic floor

Chowla, Cowles and Cowles (`MC-S36`) prove for a prime `q>3` with `q≡3 (mod 8)` that the least prime quadratic residue satisfies

\[
\ell(q)<\sqrt{q/3}
\tag{6}
\]

when the class number `h(-q)` of `Q(sqrt(-q))` exceeds one; in the class-number-one case they identify the exceptional value

\[
\ell(q)=\frac{q+1}{4}.
\tag{7}
\]

Stark's class-number-one theorem (`MC-S37`) leaves only finitely many prime discriminants in the latter case, the largest relevant prime being `163`. Hence whenever `X>=163` and `q>X`, the class-number-one branch is unavailable. Equations `(2)` and `(6)` give

\[
X<\ell(q)<\sqrt{q/3},
\]

therefore

\[
\boxed{q>3X^2.}
\tag{8}
\]

This argument is unconditional and contains no information about zeta zeros or the Mertens function.

## 3. The `q ≡ 5 (mod 8)` branch is even more expensive

Ramírez Viñas (`MC-S35`) proves that for a prime `q≡5 (mod 8)` outside

\[
\{5,13,29,37,53,101,173,197,293,677\},
\tag{9}
\]

the least prime quadratic residue satisfies

\[
\ell(q)<\frac12\sqrt{q-1}.
\tag{10}
\]

The manuscript's proof reduces the problem to the published unconditional classification of Rabinowitsch polynomials, extracts a small prime divisor of a composite polynomial value, and applies quadratic reciprocity to show that this divisor is a residue modulo `q`. The theorem is therefore used here as theorem-level literature evidence, with its preprint status explicit; no novelty is assigned to the least-residue estimate.

For `X>=677`, an exact-prefix conductor has `q>X` and so cannot belong to `(9)`. Combining `(2)` and `(10)` gives

\[
X<\frac12\sqrt{q-1},
\]

hence

\[
\boxed{q>4X^2+1.}
\tag{11}
\]

This applies directly to `MC-055`, whose CRT/Dirichlet construction deliberately chose `q_X≡5 (mod 8)`.

Combining the two residue classes proves `(4)` for every prime quadratic exact-prefix interpolant once `X>=677`.

## 4. Consequence for the cancellation certificate in MC-055

`MC-055` emphasized that each frozen comparator has a square-root **exponent** for its own summatory function. The elementary Pólya–Vinogradov/square-free decomposition used there gives a certificate of the shape

\[
\left|\sum_{n\le y}\mu(n)^2\chi(n)\right|
\ll \sqrt q\,\log q\,\sqrt y.
\tag{12}
\]

The new conductor floor shows that this standard certificate is necessarily useless at the observation scale that the character interpolates. With `y=X` and `(4)`, its right-hand scale is at least

\[
\sqrt3\,X^{3/2}\log q,
\]

before the absolute implied constant is considered, whereas the trivial coefficient bound is only `X`.

This does **not** prove that the true comparator partial sum is large. It says something narrower and operationally important: the classical frozen-character theorem that supplied the attractive `1/2` exponent in `MC-055` provides no nontrivial cancellation information at the very scale where exact Möbius-prefix agreement holds. The exponent and the conductor constant cannot be separated when the comparator moves with `X`.

Consequently a useful exact-prefix quadratic bootstrap would require a cancellation theorem whose conductor dependence remains informative at `X\lesssim\sqrt q`, or additional structure strong enough to bypass that conductor dependence. Pólya–Vinogradov alone cannot provide such a bridge.

## 5. MC-056 is correct but no longer the sharp coherence frontier here

`MC-056` compared two distinct exact-prefix interpolants and multiplied them to obtain a nonprincipal character that equals `1` on `[1,X]`. Burgess then forced

\[
q_1q_2\gg_\delta X^{4-\delta}.
\]

That deduction remains correct. The present prior-art audit changes its role.

For prime quadratic interpolants satisfying the same exact prime-prefix condition, `(4)` already gives

\[
q_1q_2>9X^4
\]

for `X>=677`, without comparing the two characters at all. In the original `q_i≡5 (mod 8)` construction, `(11)` gives the stronger constant `16` asymptotically. Thus Burgess pairwise coherence is not the first obstruction to repeatedly changing exact-prefix quadratic certificates: **least-prime-residue theory has already charged a quadratic conductor cost to each certificate individually**.

The Burgess mechanism can still be useful for broader interpolation classes where no analogous individual least-residue theorem applies. It should not, however, be treated as the sharp complexity barrier for the prime-quadratic family of `MC-055`.

## 6. Prior art and novelty boundary

The arithmetic ingredients are classical or literature-supplied:

- `MC-S36`: Chowla–Cowles–Cowles' least-prime-residue/class-number theorem for `q≡3 (mod 8)`;
- `MC-S37`: Stark's complete imaginary quadratic class-number-one determination;
- `MC-S35`: Ramírez Viñas' `q≡5 (mod 8)` least-prime-residue bound, whose proof explicitly uses the unconditional Rabinowitsch-polynomial classification and quadratic reciprocity.

A targeted search of least prime quadratic residues, class-number criteria and modern residue literature found these mechanisms directly adjacent to the `MC-055` construction. Accordingly there is no novelty claim for `(6)`, `(7)`, `(10)`, class-number finiteness, or the quadratic-residue language.

The retained Mathia result is the exact specialization to the moving Möbius-prefix comparator and the resulting correction of the research frontier: the previously identified unknown conductor relation is not wholly unknown. Exact prime-prefix matching itself forces `q=X^{2+o(1)}` or larger at the exponent level for prime quadratic characters.

## 7. Boundaries and falsification tests

The conclusion is deliberately restricted.

- It applies to **prime-conductor quadratic characters** satisfying exact `chi(p)=-1` for every prime `p<=X`. It does not automatically extend to composite conductors, higher-order characters, or general multiplicative comparators.
- The uniform statement `(4)` is asymptotic only in the harmless sense that `X>=677` removes the finite least-residue/class-number exceptions. Those small moduli have no bearing on the moving large-scale frontier.
- The result constrains conductor complexity, not the actual value of `M(X)` and not the true partial sums of the comparator beyond the matched prefix.
- Lower-bounding `q` makes the standard Pólya–Vinogradov certificate noninformative at `y=X`; it does not lower-bound the comparator partial sum itself.
- The result does not rule out a different source-forced moving family with a cancellation theorem uniform in its own complexity parameter. It does rule out treating exact quadratic-prefix interpolation plus a frozen square-root exponent as a cheap certificate.

The main claim is falsified if an exact-prefix prime quadratic character can have `(2/q)=1`, if the quoted least-prime-residue theorem does not apply under the stated congruence/class-number hypotheses, or if a large prime `q≡3 (mod 8)` can remain in the class-number-one branch. The supplementary law, `MC-S36`, and `MC-S37` exclude those possibilities; the `q≡5` strengthening rests on the explicitly identified preprint theorem `MC-S35`.

## Consequence for the active frontier

The viable moving-comparator question becomes narrower than after `MC-056`. For prime quadratic characters, **exact finite-prefix fidelity already forces the arithmetic object into conductor at least quadratic in the observed scale**, where the generic frozen-character square-root estimate loses all operational force.

A surviving comparator strategy must therefore relax at least one part of this package: exact agreement on every small prime, prime-quadratic character structure, or reliance on conductor-sensitive classical character-sum bounds. Alternatively it must supply a genuinely new uniform-family theorem that remains nontrivial at or below the square-root-of-conductor scale. Repeatedly selecting new exact quadratic characters is not merely nonuniform; classical least-residue theory shows that each selection is individually expensive.