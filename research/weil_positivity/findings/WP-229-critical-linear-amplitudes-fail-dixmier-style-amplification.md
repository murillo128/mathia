# WP-229 — Critical linear amplitudes fail Dixmier-style amplification; squaring restores trace scaling but erases repeated prime powers

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-MODES + KY-FAN-ASYMPTOTIC + MATRIX-AMPLIFICATION-OBSTRUCTION + SLOW-VARIATION-BOUNDARY + QUADRATIC-COMPLETION + TRACE-CLASS-TAIL + PRIME-POWER-BLIND-SINGULAR-RESIDUE + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-227` leaves the exact critical finite amplitudes in the matched cross channel

\[
c_{p,k}=(\log p)p^{-k/2},
\qquad p\ \text{prime},\ k\ge1,
\tag{1}
\]

and `WP-228` shows that the positive minimal companion

\[
B_{\min}=C^*C,
\qquad
b_{p,k}=(\log p)^2p^{-k},
\tag{2}
\]

lies beyond the ordinary Dixmier ideal but has second-logarithmic Ky Fan growth. The natural remaining question is whether one can keep the **linear** critical amplitudes and assign them a source-forced singular mass before they are squared, or instead use the second-logarithmic singular mass of `B_min` as the missing geometric completion.

There is a sharp dichotomy.

Let `A=|C|`, so its singular values are the numbers `c_{p,k}`. Then

\[
\boxed{
K_N(A):=\sum_{n\le N}\mu_n(A)
\sim 2\sqrt{N\log N}.
}
\tag{3}
\]

Hence every asymptotically faithful Ky-Fan normalization for the **linear** amplitudes has regular-variation ratio

\[
\frac{\psi(2N)}{\psi(N)}\longrightarrow\sqrt2.
\tag{4}
\]

This is incompatible with trace additivity under orthogonal doubling. Indeed, for even rank,

\[
K_{2N}(A\oplus A)=2K_N(A),
\tag{5}
\]

so a generalized-limit residue normalized to give a finite nonzero value on `A` gives only a factor `\sqrt2` on `A\oplus A`, whereas every trace must give a factor `2`. Therefore **no nontrivial Dixmier-style/Ky-Fan singular normalization which is finite and nonzero on the exact linear critical channel can be additive under matrix amplification**.

Squaring changes the scaling class. `WP-228` gives

\[
K_N(B_{\min})
\sim \frac12(\log N)^2,
\qquad
\frac{K_{2N}(B_{\min})}{K_N(B_{\min})}\longrightarrow1.
\tag{6}
\]

Thus the quadratic companion sits on the slowly varying side where generalized Marcinkiewicz/Dixmier trace scaling is compatible with additivity. But the price is exact arithmetic information loss. Split

\[
B_{\min}=B_1\oplus R,
\tag{7}
\]

where `B_1` is the `k=1` prime sector and `R` contains all repeated prime powers `k\ge2`. Then

\[
\boxed{
\operatorname{Tr}R
=
\sum_p\sum_{k\ge2}(\log p)^2p^{-k}
=
\sum_p\frac{(\log p)^2}{p(p-1)}
<\infty.
}
\tag{8}
\]

Consequently every second-logarithmic Ky-Fan residue of the standard generalized-limit form annihilates `R`. With the normalization `\psi(N)\sim(\log N)^2`, both the full bath and the primes-only matched control have the same generalized-limit-independent value

\[
\boxed{
\lim_{N\to\infty}\frac{K_N(B_{\min})}{\psi(N)}
=
\lim_{N\to\infty}\frac{K_N(B_1)}{\psi(N)}
=
\frac12.
}
\tag{9}
\]

Thus the singular-weight fork has a precise tradeoff:

\[
\boxed{
\text{retain the linear Weil amplitudes}
\Longrightarrow
\text{wrong amplification law for a Dixmier-style trace};
}
\tag{10}
\]

\[
\boxed{
\text{square into the positive companion}
\Longrightarrow
\text{trace-compatible slow variation, but repeated prime powers are singular-trace invisible}.
}
\tag{11}
\]

This does not rule out every singular, modular, semifinite, or distributional finite--archimedean geometry. It does rule out a much more specific and previously live shortcut: **the missing Weil-positive structure cannot be obtained merely by promoting either the linear critical mode list or its minimal quadratic bath to a scalar Dixmier/Marcinkiewicz-type singular residue.** A surviving construction must use additional relational structure before the final positive readout.

## 1. The linear critical channel has square-root Ky Fan growth

Write the prime-power mode space as the orthogonal union of exponent sectors `k=1,2,3,...`. For `k=1`, the singular values are

\[
a_p=\frac{\log p}{\sqrt p}.
\tag{12}
\]

After finitely many terms this is decreasing in `p`. If `p_n` is the `n`-th prime, the prime number theorem gives

\[
p_n\sim n\log n,
\qquad
\log p_n\sim\log n,
\tag{13}
\]

and therefore

\[
a_{p_n}
\sim
\sqrt{\frac{\log n}{n}}.
\tag{14}
\]

The sequence on the right is regularly varying with index `-1/2`, hence summation (or a direct integral comparison) gives

\[
\sum_{n\le N}a_{p_n}
\sim
2\sqrt{N\log N}.
\tag{15}
\]

The `k=2` sector is lower order. Its `n`-th prime value is

\[
\frac{\log p_n}{p_n}
\sim\frac1n,
\tag{16}
\]

so its first `N` terms have total `\sim\log N`. Every sector `k\ge3` is absolutely summable even after all primes are included:

\[
\sum_p\sum_{k\ge3}(\log p)p^{-k/2}
=
\sum_p
\frac{(\log p)p^{-3/2}}{1-p^{-1/2}}
<\infty.
\tag{17}
\]

For a union of decreasing positive sequences, the sum of the `N` largest terms is bounded above by the sum of the first `N` terms from each component sequence. Hence the `k=2` and `k\ge3` sectors contribute only `O(\log N)` and `O(1)` to the upper bound, while the `k=1` sector alone supplies the lower bound (15). This proves (3).

The result is not another statement that `C\notin S_2`; `WP-228` already has that. Equation (3) identifies the exact **additive scaling law** of the linear channel, which is what a Dixmier-style singular trace would have to respect.

## 2. Orthogonal doubling falsifies a linear-amplitude Dixmier residue

Let `\psi` be any positive normalization for which

\[
\frac{K_N(A)}{\psi(N)}\longrightarrow L,
\qquad 0<L<\infty.
\tag{18}
\]

By (3), necessarily

\[
\psi(N)\sim \frac{2}{L}\sqrt{N\log N},
\tag{19}
\]

so

\[
\frac{\psi(2N)}{\psi(N)}\longrightarrow\sqrt2.
\tag{20}
\]

Now duplicate the same source channel orthogonally. Because every singular value of `A` appears twice in `A\oplus A`, exactly

\[
K_{2N}(A\oplus A)=2K_N(A).
\tag{21}
\]

Therefore

\[
\frac{K_{2N}(A\oplus A)}{\psi(2N)}
\longrightarrow
\frac{2L}{\sqrt2}
=
\sqrt2\,L.
\tag{22}
\]

Any generalized limit applied to these already convergent normalized means gives the same value. But a trace `\tau` must satisfy matrix-amplification additivity

\[
\tau(A\oplus A)=2\tau(A)=2L.
\tag{23}
\]

Since `\sqrt2 L\ne2L`, the Ky-Fan residue cannot be a trace.

This also removes a normalization loophole. A normalization growing faster than (19) gives zero on `A`; one growing slower gives no finite value. Every normalization producing a finite nonzero source mass has the same `\sqrt2` doubling ratio and fails the same test.

The calculation is the concrete source-specific manifestation of the classical slow-variation boundary in Marcinkiewicz/Dixmier trace theory. No novelty is claimed for that general operator-ideal theorem. What is new here is that the exact Bost--Connes critical linear mode carrier forced by `WP-216`/`WP-227` lands on the **wrong side** of that boundary.

## 3. Squaring repairs amplification but removes the repeated-prime-power tail

For `B_min=A^2`, `WP-228` proves

\[
K_N(B_{\min})
\sim\frac12(\log N)^2.
\tag{24}
\]

The corresponding gauge is slowly varying:

\[
\frac{(\log 2N)^2}{(\log N)^2}\longrightarrow1.
\tag{25}
\]

Accordingly, orthogonal doubling now has the trace-compatible leading law

\[
\frac{K_{2N}(B_{\min}\oplus B_{\min})}{(\log 2N)^2}
=
\frac{2K_N(B_{\min})}{(\log 2N)^2}
\longrightarrow1
=
2\cdot\frac12.
\tag{26}
\]

So the problem identified in Section 2 really is removed by passing to the positive quadratic companion; it is not a generic objection to singular traces.

However, the same squaring isolates the entire repeated-prime-power tower inside the trace-class remainder (8). For any standard second-logarithmic generalized-limit residue

\[
\tau_{\omega,\psi}(T)
=
\omega\!\left(
\frac{K_N(T)}{\psi(N)}
\right),
\qquad
\psi(N)\sim(\log N)^2,
\tag{27}
\]

whenever the usual compatibility assumptions make this a trace, a positive trace-class operator `S` has

\[
0\le
\frac{K_N(S)}{\psi(N)}
\le
\frac{\operatorname{Tr}S}{\psi(N)}
\longrightarrow0.
\tag{28}
\]

Hence `\tau_{\omega,\psi}(R)=0`. Equations (24) and (8) then give (9) directly. The result is independent of the generalized limit because the normalized means already converge ordinarily.

This is stronger than saying the leading coefficient comes from prime density. It says the full `k\ge2` source tower is **exactly null in the singular quotient used by the second-logarithmic residue**.

## 4. Matched controls show what the singular residue forgets

The first control deletes every repeated prime power while retaining all prime modes:

\[
B_{\mathrm{prime}}e_{p,1}
=
\frac{(\log p)^2}{p}e_{p,1},
\qquad
B_{\mathrm{prime}}e_{p,k}=0\quad(k\ge2).
\tag{29}
\]

Then

\[
B_{\min}-B_{\mathrm{prime}}=R\in\mathcal S_1,
\tag{30}
\]

so every residue in (27) gives the same value to the exact source bath and the primes-only control.

More generally, the entire `k\ge2` sector may be replaced by any other positive trace-class diagonal tail without changing the singular residue. Thus this functional cannot distinguish the actual Bost--Connes prime-power tower from infinitely many matched tails once their `k=1` sector is fixed.

The same loss is visible in the source Hamiltonian cutoff of `WP-228`. If

\[
R(T)=\sum_{k\log p\le T}(\log p)^2p^{-k}
\tag{31}
\]

and `R_1(T)` keeps only `k=1`, then (8) gives

\[
0\le R(T)-R_1(T)\le\operatorname{Tr}R=O(1),
\tag{32}
\]

while both have leading growth `T^2/2`. The prime-power blindness is therefore not an artifact of ordering eigenvalues by size.

This is a decisive matched control for the research mandate because the finite Weil explicit formula does distinguish every prime power through

\[
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
(\log p)p^{-k/2},
\qquad k\ge1.
\tag{33}
\]

A scalar singular residue which is unchanged after deleting all `k\ge2` modes cannot itself be the structure that explains the full finite-place Weil term.

## 5. What remains possible

The theorem does **not** say that the full matched positive block of `WP-227` is useless. Its cross channel `C` still contains every exact coefficient (1). Nor does it exclude a geometry in which a singular weight is only one component of a larger finite--archimedean construction.

The excluded shortcut is narrower and more useful: one cannot obtain the missing global mechanism by simply declaring a Ky-Fan/Marcinkiewicz singular residue of the source mode amplitudes to be the positive arithmetic integral. At the linear level, trace amplification fails. At the quadratic level, trace-compatible normalization is available but the residue has already quotiented out every repeated prime power and squared the desired amplitudes.

A surviving route must therefore perform at least one genuinely additional operation **before** the final scalar positive readout: for example, an active finite--archimedean incidence coupling, a modular/semifinite form whose weight is not a Ky-Fan singular residue, a nontracial positive pairing, or a source-forced finite-part construction that retains the trace-class prime-power tail. Any finite part must itself be canonical and pass the sign, Gamma/polar, and matched-control gates; arbitrary subtraction of the leading singular mass is not evidence of Weil positivity.

## 6. Prior-art and novelty boundary

The general relation between Marcinkiewicz gauges, slow variation, fully symmetric functionals, and Dixmier traces is classical operator-ideal theory. `WP-228` already records that prior-art boundary and explicitly refuses to claim a new singular-trace theorem. The matrix-amplification contradiction in Section 2 is an elementary concrete version of the same classical phenomenon.

The Bost--Connes system, its logarithmic Hamiltonian, spectral-triple variants, and noncommutative-geometric approaches to Weil positivity are likewise established prior art already anchored by this line. A bounded literature audit around Bost--Connes spectral triples, generalized Marcinkiewicz/Dixmier traces, and Connes--Consani quantized-calculus/Weil-positivity work did not expose the exact `WP-227` critical mode carrier or the dichotomy (10)--(11) as a published result.

The durable Mathia-specific content is therefore the combination of three exact source facts:

1. the **linear** matched critical channel has `K_N\sim2\sqrt{N\log N}` and fails the orthogonal-doubling law required by any finite nonzero Ky-Fan/Dixmier-style trace normalization;
2. squaring to the minimal positive companion changes the gauge to the slowly varying `K_N\sim(1/2)(\log N)^2`, so the amplification obstruction disappears;
3. the same squaring makes every repeated-prime-power contribution trace class, hence invisible to the resulting second-logarithmic singular residue.

This is a negative/narrowing result, not a new global positive form. It proves no part of RH and supplies neither the Gamma factor nor the polar terms.

## 7. Consequence for the active Bost--Connes completion clue

The accepted Bost--Connes completion direction remains open, but its singular-weight branch is narrower than after `WP-228`. A viable source-forced completion cannot rely on a scalar Ky-Fan/Marcinkiewicz residue of `C` or `C^*C` alone. It must preserve the exact linear prime-power data through additional relational structure and only then obtain positivity from a theorem that also generates the archimedean and polar sectors.

The next decisive test is therefore not to search for a different generalized limit on the same critical mode list. It is to exhibit a concrete nontracial/modular or finite--archimedean coupling whose defining law is source-forced before the Weil sign is evaluated, and to show on matched controls that it retains `k\ge2` arithmetic rather than collapsing to the prime-only singular quotient.