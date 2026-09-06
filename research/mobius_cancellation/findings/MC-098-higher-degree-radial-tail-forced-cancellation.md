# MC-098 — Higher radial degrees are forced to cancel the degree-two main term

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the product-fiber radial shell sums from `MC-092` and `MC-097` be

\[
C_{k,N}:=\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a),
\]

so that the Möbius endpoint of the prime-symmetric-difference/Huxley--Watt deformation is

\[
\mathcal Q_N(1)=\sum_{k\ge0}(-1)^k C_{k,N}.
\tag{1}
\]

`MC-097` proves

\[
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\qquad
c_2=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0.
\tag{2}
\]

The possibility left open there is not merely hypothetical. Classical unconditional cancellation for the Mertens function forces the **aggregate higher-degree radial tail** to cancel this positive main term. Put

\[
T_{\ge3}(N):=\sum_{k\ge3}(-1)^k C_{k,N}.
\tag{3}
\]

Then

\[
\boxed{
T_{\ge3}(N)
\sim
-c_2\frac{N^2}{(\log N)^2}.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
C_{2,N}+T_{\ge3}(N)
=o\!\left(\frac{N^2}{(\log N)^2}\right).
}
\tag{5}
\]

In fact, using the standard Korobov--Vinogradov zero-free-region bound recorded in `MC-S3`, the endpoint itself is smaller than `N^2/(\log N)^A` for every fixed `A>0`. Since the degree-zero and degree-one shells are also negligible compared with `(2)`, the cancellation in `(4)` is unconditional and occurs before any RH-scale input.

Consequently,

\[
\boxed{
\sum_{k\ge3}|C_{k,N}|
\ge
|T_{\ge3}(N)|
\sim
c_2\frac{N^2}{(\log N)^2}.
}
\tag{6}
\]

Thus the radial quotient has a concrete source-level pathology for positive shell norms: it contains almost-full-square-scale mass in degree two **and** almost-full-square-scale aggregate mass in higher degrees, while their alternating coupling cancels to an endpoint that is smaller than every fixed inverse power of `log N`. Taking absolute values, an `ell_p` shell norm, or any other positive degreewise estimate before this cancellation necessarily destroys a cancellation already known to occur unconditionally.

No improved estimate for `M(x)` is claimed. The result uses the classical unconditional Mertens bound as an input and only sharpens what the `MC-097` radial-shell obstruction means for the actual source vector.

## 1. Exact endpoint identity for the radial shells

`MC-092` gives the finite product-fiber decomposition

\[
\mathcal Q_N(t)
=
\sum_a W_N(a)(-t)^{\omega(a)}.
\tag{7}
\]

Grouping by degree gives

\[
\mathcal Q_N(t)=\sum_k(-t)^kC_{k,N},
\tag{8}
\]

and hence `(1)` at `t=1`.

The same endpoint is the full Möbius Huxley--Watt sawtooth block. In the notation of `MC-084`, with

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

the exact source identity is

\[
\boxed{
\mathcal Q_N(1)
=
2M(N)-M(N^2)-N^2H(N)^2+\frac12M(N)^2.
}
\tag{9}
\]

This identity is classical Huxley--Watt structure (`MC-S24`); no shell cancellation has yet been estimated in deriving it.

## 2. The classical zero-free region makes the endpoint logarithmically tiny

The unconditional comparison source `MC-S3` records that for some `c>0`,

\[
M(x)
\ll
x\exp\!\left(
-c(\log x)^{3/5}(\log\log x)^{-1/5}
\right).
\tag{10}
\]

Write

\[
\Phi(x):=(\log x)^{3/5}(\log\log x)^{-1/5}.
\]

The same classical PNT/zero-free-region input gives

\[
\sum_{n\ge1}\frac{\mu(n)}n=0.
\tag{11}
\]

Partial summation therefore yields

\[
H(N)
=
\frac{M(N)}N-
\int_N^\infty\frac{M(t)}{t^2}\,dt.
\tag{12}
\]

Using `(10)` in the tail and putting `u=\log t`,

\[
\int_N^\infty\frac{|M(t)|}{t^2}\,dt
\ll
\int_{\log N}^\infty
\exp\!\left(-c u^{3/5}(\log u)^{-1/5}\right)du.
\tag{13}
\]

A standard tail estimate for this stretched exponential, after weakening the positive constant, gives

\[
H(N)
\ll
\exp\!\left(-c_1\Phi(N)\right)
\tag{14}
\]

for some `c_1>0`. In particular, `(10)` and `(14)` imply from `(9)` that for some `c_2'>0`,

\[
\boxed{
\mathcal Q_N(1)
\ll
N^2\exp\!\left(-c_2'\Phi(N)\right).
}
\tag{15}
\]

Hence, for every fixed `A>0`,

\[
\boxed{
\mathcal Q_N(1)=O_A\!\left(\frac{N^2}{(\log N)^A}\right).
}
\tag{16}
\]

Only an unconditional zero-free region is used. No RH-strength estimate enters `(15)` or `(16)`.

## 3. Degrees zero and one cannot absorb the degree-two main term

For degree zero, `a=1`. The divisor-count factor in the product-fiber coefficient is then exactly one for every square-free `b<=N`, so

\[
C_{0,N}=W_N(1)
=
\sum_{\substack{b\le N\\b\ \mathrm{squarefree}}}
 z\!\left(\frac{N^2}{b^2}\right).
\tag{17}
\]

Since `|z|<=1/2`,

\[
\boxed{|C_{0,N}|\le \frac N2.}
\tag{18}
\]

For degree one, `MC-096` proves the stronger absolute estimate

\[
\sum_{\omega(a)=1}|W_N(a)|
\le
N\sum_{p\le N}\frac1p
=
N\log\log N+O(N).
\tag{19}
\]

Therefore

\[
\boxed{C_{1,N}=O(N\log\log N).}
\tag{20}
\]

Both `(18)` and `(20)` are

\[
o\!\left(\frac{N^2}{(\log N)^2}\right).
\tag{21}
\]

Thus neither of the two lower radial shells has enough mass to cancel the degree-two asymptotic `(2)`.

## 4. Forced cancellation by the higher-degree tail

Split the exact endpoint `(1)` at degree two:

\[
\mathcal Q_N(1)
=C_{0,N}-C_{1,N}+C_{2,N}+T_{\ge3}(N).
\tag{22}
\]

Rearranging,

\[
T_{\ge3}(N)
=
\mathcal Q_N(1)-C_{0,N}+C_{1,N}-C_{2,N}.
\tag{23}
\]

Take `A>2` in `(16)`. Equations `(18)`, `(20)`, and `(21)` show that the first three terms on the right of `(23)` except `-C_{2,N}` are all

\[
o\!\left(\frac{N^2}{(\log N)^2}\right).
\]

Inserting the positive asymptotic `(2)` proves `(4)` and `(5)`.

The triangle inequality applied to `(3)` then gives `(6)`. Thus the higher shells are not collectively small in any positive shell norm: their signed alternating aggregate already has the same `N^2/(\log N)^2` scale as degree two.

## 5. What this changes in the radial-shell frontier

`MC-097` proves that an `ell_2`-then-Cauchy treatment of the individual radial shells cannot work because degree two alone has size `N^2/(\log N)^2`. The present result identifies the missing cancellation more sharply: **the actual Huxley--Watt source unconditionally arranges a compensating higher-degree tail of the same leading scale.**

This distinguishes two statements that should not be conflated:

1. shellwise positivity or norm control is too lossy;
2. the radial degree variable itself is useless.

Only the first is established. The second does not follow, because `(4)` shows that the degree variable carries a real, highly structured cancellation between low and high degrees. A surviving radial strategy would have to estimate a signed coupling across degrees before applying a positive norm, or derive a recurrence/transform that preserves the cancellation in `(22)`. Merely proving each `C_{k,N}` small is now impossible already at `k=2`, and merely proving a positive aggregate bound throws away an unconditional cancellation of relative logarithmic strength.

The result also sharpens the matched-control interpretation. `MC-034` and `MC-092` show critical-power RMS under random multiplicative prime signs at the full product-fiber level. Equation `(4)` is instead a deterministic identity-level consequence for the actual all-minus Möbius point after radialization. The two facts do not imply one another and should not be merged into a probabilistic explanation.

## 6. Prior art and novelty boundary

The external ingredients are classical: the Huxley--Watt finite identity (`MC-S24`), the Korobov--Vinogradov Mertens bound (`MC-S3`), the PNT consequence `(11)`, and partial summation. `MC-092` supplies the exact product-fiber/radial decomposition, `MC-096` supplies the degree-one absolute bound, and `MC-097` supplies the degree-two asymptotic.

A targeted literature search around Huxley--Watt Mertens identities combined with `omega`-shell decompositions, reciprocal sawtooth radial shells, and degreewise Möbius cancellation found the original Huxley--Watt source and adjacent Mertens literature but no basis for claiming a distinct external theorem in the exact formulation `(4)`. **No novelty claim is made.** The durable line-specific result is the composition of already audited source identities with the unconditional Mertens estimate, which turns the previously possible cross-degree cancellation into a forced asymptotic statement for this exact radial quotient.

## 7. Boundaries and falsification tests

- Equation `(4)` is only an aggregate statement over all degrees `k>=3`. It does not identify which individual shell, parity class of shells, or range of `k` supplies the compensating mass.
- The result does not estimate the endpoint more strongly than classical zero-free-region theory; `(15)` is an input-derived consequence, not a new Mertens bound.
- It does not show that cross-degree cancellation can be controlled by an independently weaker statistic. A proposed transform or recurrence still has to preserve the sign coupling without reconstructing the Mertens endpoint as an input.
- The asymptotic `(4)` depends on the full radial shells of the exact `MC-092` source vector. It does not automatically transfer to a truncated Fourier kernel, altered sawtooth, block-count quotient, or random multiplicative comparator.
- The use of `(11)` is classical PNT information. A matched model without the corresponding vanishing reciprocal sum need not satisfy `(14)` or `(4)`.
- The result would fail if the endpoint identity `(9)`, the low-degree estimates `(18)`--`(20)`, or the degree-two main term `(2)` were incorrect. Each is independently auditable in the cited canonical findings/sources.

## Consequence for the research line

The radial-shell branch has crossed a useful threshold. `MC-095`--`MC-097` showed that radialization loses product-fiber orthogonality and that the degree-two shell is intrinsically huge. `MC-098` now shows that **large cross-degree cancellation is not merely a hoped-for escape; it is already forced by unconditional arithmetic**.

The remaining question is therefore narrower and more structural: can the exact cancellation in `(22)` be exposed by a source-natural signed cross-degree carrier that is independently controllable, rather than by estimating shells separately or by bounding the full endpoint in disguise? Any candidate that applies an absolute value or positive shell norm before coupling degree two to the higher tail has already discarded a cancellation of order `N^2/(\log N)^2` that the actual Möbius source demonstrably performs.