# AF-343 — periodic backgrounds cannot reduce the prime-layer sign order

**Status:** `EXACT-DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-GATE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-342 shows that a variable background can lower the ordered sign variation of the centered prime layer only by reacting on a prime-scale set of prime sites or prime-adjacent composite sites. That local cover leaves an obvious cheap-looking loophole: a nonconstant background may have a fixed, low-description zero pattern, so many prime neighbors disappear under the zero-deletion convention without the background encoding the primes individually.

That loophole fails for every fixed periodic background.

Let

\[
a(n):=
\begin{cases}
\log p,&n=p\text{ prime},\\
0,&\text{otherwise},
\end{cases}
\qquad
h_b(n):=a(n)-b(n),
\tag{1}
\]

and count ordered sign changes after deleting zero coefficients, as in AF-216 and AF-342.

First, a general source-side statement is useful. Assume that for all sufficiently large integers

\[
b(n)\ge0,
\tag{2}
\]

that for every sufficiently large prime

\[
b(p)<\log p,
\tag{3}
\]

and that there is a fixed integer `K>=1` such that every interval of `K` consecutive sufficiently large integers contains a composite `m` with

\[
b(m)>0.
\tag{4}
\]

Then for every fixed `B>1`, with `U=\lfloor BP\rfloor`, one has

\[
\boxed{
\frac{2}{K}\bigl(\pi(U)-\pi(P-1)\bigr)-2
\;\le\;
V\bigl(h_b(P),\ldots,h_b(U)\bigr)
\;\le\;
2\bigl(\pi(U)-\pi(P-1)\bigr)+2.
}
\tag{5}
\]

Consequently the prime number theorem gives

\[
\boxed{
V\bigl(h_b(P),\ldots,h_b(\lfloor BP\rfloor)\bigr)
=\Theta_b\!\left(\frac{P}{\log P}\right).
}
\tag{6}
\]

Thus a background whose negative residual witnesses remain **syndetic** cannot change the order of the prime-layer sign burden. To obtain

\[
V=o(P/\log P),
\tag{7}
\]

the composite set on which `b(m)>0` must develop unbounded holes along some sequence of multiplicative windows, or the background must instead rise to prime height on a prime-scale set as in AF-342. Fixed local structure is not enough.

Now let `b` be a nonnegative periodic sequence of period `q` with positive mean. Then `b` is bounded, so `(3)` holds automatically for large primes. Moreover `(4)` holds for some `K=K(q,b)` depending only on the period and on one positive residue class. Hence every such periodic background satisfies `(6)`.

The analytically normalized case is especially sharp. If

\[
\frac1q\sum_{r=1}^{q} b(r)=1,
\tag{8}
\]

then

\[
B_b(s):=\sum_{n\ge2}b(n)n^{-s}
\tag{9}
\]

extends meromorphically to the whole complex plane with only a simple pole at `s=1`, of residue `1`. Therefore, with the prime-layer transform `A(s)` from AF-341,

\[
H_b(s):=A(s)-B_b(s)
\tag{10}
\]

is holomorphic at `s=1` and has residue `-m` at every zeta zero `rho` with `Re(rho)>1/2` and multiplicity `m`. Thus

\[
\boxed{
\mathrm{RH}
\iff
H_b\text{ is holomorphic on }\Re(s)>\tfrac12.
}
\tag{11}
\]

So normalized periodic backgrounds are an explicit family of **cheap, nonconstant, zero-pole-blind baselines that preserve the RH right-half-plane pole discriminator but provably cannot reduce the source sign complexity below `Theta(P/log P)`**.

## Derivation

### 1. Syndetic negative witnesses force prime-scale sign variation

Under `(2)`--`(3)`, for every sufficiently large prime `p`,

\[
h_b(p)=\log p-b(p)>0.
\tag{12}
\]

For a composite integer `m`,

\[
h_b(m)=-b(m)\le0,
\tag{13}
\]

and it is strictly negative exactly when `b(m)>0`.

After zero coefficients are deleted, every positive nonzero entry is therefore a prime and every site supplied by `(4)` is a negative nonzero entry.

Consider one positive run in the zero-deleted sign sequence. If that run spanned `K` consecutive integer positions, `(4)` would place a negative nonzero composite site inside the span, splitting the run. Hence every positive run contains at most `K` prime sites.

Let

\[
N(P,U):=\pi(U)-\pi(P-1).
\tag{14}
\]

If `R(P,U)` is the number of positive runs after zero deletion, then

\[
R(P,U)\ge \frac{N(P,U)}{K}.
\tag{15}
\]

Every interior positive run contributes two sign changes. Only the two boundary runs can lose one transition each, so

\[
V\ge2R-2\ge\frac{2N(P,U)}{K}-2.
\tag{16}
\]

Conversely every sign change is incident to a positive run, and there are at most `N(P,U)` positive runs. Thus

\[
V\le2N(P,U)+2.
\tag{17}
\]

This proves `(5)`. Applying the prime number theorem on `[P,BP]` proves `(6)`.

The quantitative content is the contrapositive: any source recoding that really lowers this sign currency must destroy every fixed syndetic bound for negative composite witnesses, unless it neutralizes the prime coefficients themselves. AF-342 detects the nearest-neighbor version of that cost; `(5)` shows that replacing those neighbors by a fixed periodic pattern merely pushes the witnesses a bounded distance away and does not change the asymptotic order.

### 2. Every nontrivial nonnegative periodic background has syndetic composite support

Let `b` have period `q` and positive mean. Choose a residue `r mod q` with

\[
b(r)>0.
\tag{18}
\]

Choose a prime `ell` with `ell` not dividing `q`. Because multiplication by `q` is invertible modulo `ell`, among any `ell` consecutive terms

\[
n_0,\ n_0+q,\ldots,\ n_0+(\ell-1)q
\tag{19}
\]

in the residue class `r mod q`, exactly one is divisible by `ell`.

For sufficiently large `n_0`, that divisible term is strictly larger than `ell`, hence composite. Starting from any sufficiently large integer `x`, the first integer `n_0>=x` congruent to `r mod q` lies less than `q` steps away, and the divisible term in `(19)` lies within a further `(ell-1)q` steps. Therefore there is a constant, for example

\[
K=q(\ell+1),
\tag{20}
\]

such that every `K`-term interval sufficiently far out contains a composite `m` with `b(m)=b(r)>0`.

Since a periodic sequence is bounded, say `0<=b(n)<=M`, every prime `p>e^M` satisfies `b(p)<log p`. Thus the hypotheses of the syndetic theorem hold and `(6)` follows.

This argument also covers eventually periodic backgrounds: a finite initial defect changes neither the eventual syndeticity nor the asymptotic sign order.

### 3. Periodic Dirichlet series are zero-pole-blind after mean normalization

For an exactly `q`-periodic sequence, the Dirichlet series can be written, up to the harmless finite correction caused by starting at `n=2`, as

\[
B_b(s)
=q^{-s}\sum_{r=1}^{q} b(r)\,\zeta\!\left(s,\frac rq\right)+\text{entire finite correction},
\tag{21}
\]

where `zeta(s,alpha)` is the Hurwitz zeta function.

Each Hurwitz zeta function extends meromorphically to the whole plane with only a simple pole at `s=1`, of residue `1`. Therefore `B_b` has only the simple pole

\[
\operatorname*{Res}_{s=1}B_b(s)
=\frac1q\sum_{r=1}^{q}b(r).
\tag{22}
\]

Under `(8)` this residue is `1`, and `B_b` has no poles at zeta zeros.

AF-341 gives the meromorphic continuation of

\[
A(s)=\sum_p(\log p)p^{-s}
\tag{23}
\]

to `Re(s)>1/2`, with residue `+1` at `s=1` and residue `-m` at each zeta zero `rho` in that half-plane. Subtracting the normalized periodic `B_b` cancels the pole at `1` and cannot cancel a zero pole. This proves `(11)`.

The family therefore passes the analytic-fidelity test and fails the source-complexity test simultaneously. The failure is not because the baseline was constant: every fixed periodic nonconstant recoding has the same asymptotic obstruction.

## Consequence for the AF-342 frontier

AF-342 leaves open a canonical variable or multiscale baseline whose exceptional structure is generated from cheaper retained data. Periodicity is the cleanest finite-description test of that escape because it can create infinitely many zero/nonzero exceptions from only finitely many retained coefficients.

AF-343 rules out that entire class. A periodic support mask can indeed erase all immediate prime neighbors for some residue patterns, making AF-342's nearest-neighbor exceptional cover large, but the erased negative witnesses reappear within a bounded distance. After zero deletion, each positive run can contain only boundedly many primes, so the total sign order remains `Theta(P/log P)`.

The live escape is therefore genuinely multiscale or arithmetic. To beat the sign order without neutralizing prime coefficients, the background's positive composite support must acquire holes whose lengths are not uniformly bounded. A fixed finite-period mask, and more generally any baseline satisfying the syndetic negative-witness condition `(4)`, cannot do it.

This is still a source-side obstruction. It does not prove that every useful RH-facing representation must pay `P/log P` complexity in some universal sense, and it does not supply the growing-order observation theorem missing after AF-338.

## Exact controls and boundaries

### Periodicity is sufficient for the no-go, not necessary

The real hypothesis behind `(5)` is syndeticity of negative composite witnesses, not periodicity. Aperiodic, automatic, substitutional, or dynamically generated backgrounds may also satisfy `(4)` and are then covered automatically. No claim is made here that every low-description sequence is syndetic.

### The theorem does not price description length

A periodic background has finite description complexity, while its residual still has prime-scale ordered sign variation. Conversely an aperiodic background with unbounded witness gaps might still be generated by a short rule. Equation `(5)` is a geometric/source-order obstruction, not a Kolmogorov-, circuit-, entropy-, or bit-complexity lower bound.

### Nonnegativity matters

If `b` is allowed to take negative values on composites, then positive residual composite sites appear and the clean identification of positive runs with prime runs fails. Such sign-changing baselines may have larger variation automatically, but they require a separate accounting if they are proposed as a simplification mechanism.

### Fixed period matters

A family whose period `q=q(P)` grows with the observation scale can have `K=K(P)` growing as well, and `(5)` then weakens proportionally. AF-343 therefore rules out fixed periodic/fixed-syndetic repairs, not a genuinely multiscale baseline with increasing structural resolution.

### Mean normalization is the analytic bridge

Equation `(6)` needs only the source-side assumptions `(2)`--`(4)`. The mean-one condition `(8)` is needed only for the RH pole-discriminator statement `(11)`. A periodic background of another mean still has the same sign-order obstruction but leaves an uncancelled pole at `s=1`.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- The meromorphic continuation of the Hurwitz zeta function, with its unique simple pole of residue `1` at `s=1`, is classical; see the *Encyclopedia of Mathematics*, **“Hurwitz zeta function”**, and Apostol, *Introduction to Analytic Number Theory*, Chapter 12.
- NIST DLMF §27.10 records the standard finite-Fourier description of periodic number-theoretic functions. Equation `(21)` is the direct residue-class decomposition of the associated ordinary Dirichlet series into Hurwitz zeta functions.
- The prime number theorem and the prime-layer continuation/pole structure are the classical ingredients already audited in AF-341 through Titchmarsh and the logarithmic derivative of zeta.

A targeted literature search did not identify the exact sign-run statement `(5)` or its use as a periodic-background obstruction for this prime-layer fidelity problem. The result is nevertheless recorded as an exact derived synthesis of classical ingredients, not as a novelty claim.

The Arithmetic Fidelity contribution is the **multiscale resource accounting**: a fixed periodic mask can manufacture infinitely many zero sites from finite retained data, but bounded-distance negative witnesses survive and force the same prime-scale sign order. Any successful baseline repair must therefore introduce growing spatial resolution, neutralize a prime-scale set of prime coefficients, or abandon ordered sign variation as the downstream source certificate.