# XF-089 — Polymath reference freezes the positive-time endpoint pole

**Status:** `LITERATURE+DERIVED` + `POSITIVE-TIME-ENDPOINT` + `REFERENCE-RENORMALIZATION` + `BRIDGE-REDUCTION`. XF-088 shows that the endpoint carrier at `t=0` cannot be fed directly into the periodic Volterra trapezoid: the universal pole

\[
\mathcal Z_0(\xi)=-\frac1{4\xi}+O(1)
\]

forces the mesh counterterm `(1/4) log Delta delta_0`. The unresolved dynamic question was whether positive heat time changes that degree-`-1` singular sector, which would require a time-dependent endpoint renormalization before XF-087 could be used over a nonzero heat interval.

It does not. The effective Polymath15 asymptotic reference already contains the complete positive-time degree-`-1` sector, and its residue is independent of heat time. More precisely, choose any fixed horizontal height

\[
3<a<4,
\qquad
s_a(x):=\frac{1+a-ix}{2}.
\]

Let `M_t` be the explicit Polymath15 reference

\[
M_t(s)=\exp\!\left(\frac t4\alpha(s)^2\right)M_0(s),
\qquad
\alpha(s):=(\log M_0)'(s)
=
\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi},
\tag{1}
\]

and put

\[
B_{t,a}(x):=M_t(s_a(x)).
\]

For `0<t<=1/2`, Proposition 9.1(ii) of D. H. J. Polymath gives, uniformly for sufficiently large positive `x` and `3<=a<=4`,

\[
H_t(x+ia)=B_{t,a}(x)(1+\varepsilon_{t,a}(x)),
\qquad
|\varepsilon_{t,a}(x)|\le0.7.
\tag{2}
\]

The conjugation symmetry gives the same control at the negative end. Since both `H_t` and `B_{t,a}` are zero-free on this horizontal strip, the quotient admits a bounded logarithm on the chosen line. Define

\[
L_{t,a}(x):=\log\frac{H_t(x+ia)}{B_{t,a}(x)}.
\tag{3}
\]

Then, after fixing the continuous branch, `L_{t,a}` is bounded on the real axis. The tails are bounded directly by (2), while the remaining compact interval is harmless because the quotient is continuous and nonzero.

Now differentiate. The actual logarithmic derivative and the reference logarithmic derivative satisfy

\[
Q_a(x,t):=\frac{H_t'(x+ia)}{H_t(x+ia)},
\qquad
Q^M_a(x,t):=\partial_x\log B_{t,a}(x),
\]

and therefore

\[
\boxed{
Q_a-Q^M_a=\partial_x L_{t,a}.
}
\tag{4}
\]

With the XF-051 Fourier convention and carrier normalization,

\[
\mathcal Z_t(\xi)=\frac{i}{2\pi}e^{a\xi}\widehat Q_a(\xi,t),
\qquad \xi>0,
\]

define analogously

\[
\mathcal Z^M_t(\xi)
:=
\frac{i}{2\pi}e^{a\xi}\widehat {Q^M_a}(\xi,t).
\]

Fourier transforming (4) gives the exact positive-frequency identity

\[
\boxed{
\mathcal Z_t(\xi)-\mathcal Z^M_t(\xi)
=
-\frac{\xi}{2\pi}e^{a\xi}\widehat L_{t,a}(\xi),
\qquad \xi>0.
}
\tag{5}
\]

Thus the Xi/reference residual carries an **exact factor of `xi`**. This is the positive-time analogue of subtracting the deterministic endpoint background, but it is stronger than merely matching the leading asymptotic coefficient: the residual is the Fourier derivative of a bounded primitive.

The explicit reference itself has endpoint normal form

\[
\boxed{
\mathcal Z^M_t(\xi)
=
-\frac{e^{-\xi}}{4\xi}
-
\frac t8 e^{-\xi}
\left(\log\xi+\gamma+\log(4\pi)\right)
+O_t(1),
\qquad \xi\downarrow0.
}
\tag{6}
\]

In particular,

\[
\boxed{
\operatorname*{Res}_{\xi=0^+}\mathcal Z^M_t=-\frac14
\quad\text{for every }0\le t\le\frac12.
}
\tag{7}
\]

Because the residual (5) has a bounded physical-space primitive, it cannot contribute another open-half-line `1/xi` term: such a term would require `\widehat L_{t,a}` to contain a degree-`-2` singularity at zero, whose inverse Fourier transform has linear growth, contradicting boundedness of `L_{t,a}`. Hence the same residue holds for the actual Xi carrier:

\[
\boxed{
\mathcal Z_t(\xi)
=
-\frac1{4\xi}
+\text{strictly lower endpoint order},
\qquad
0\le t\le\frac12.
}
\tag{8}
\]

The `t=0` endpoint is independently exact from XF-052. Therefore the logarithmic lattice counterterm isolated by XF-088 has a **time-independent coefficient** throughout the whole classical de Bruijn interval:

\[
\boxed{
\frac14\log\Delta\,\delta_0.
}
\tag{9}
\]

Positive heat time does create a new deterministic logarithmic cusp, whose leading coefficient is `-t/8`, but it does not create a new pole or alter the pole counterterm.

## 1. Derivation of the explicit reference endpoint

From (1),

\[
\partial_x\log B_{t,a}(x)
=
-\frac i2
\left[
\alpha(s_a(x))
+\frac t2\alpha(s_a(x))\alpha'(s_a(x))
\right].
\tag{10}
\]

Put `b=1+a`. As `|x|->infinity` in the fixed horizontal strip,

\[
\alpha(s)
=
\frac12\Log\frac{s}{2\pi}
+\frac{3}{2s}
+O(s^{-2}),
\qquad
\alpha'(s)
=
\frac1{2s}+O(s^{-2}),
\tag{11}
\]

so

\[
Q^M_a(x,t)
=
-\frac i4\Log\frac{b-ix}{4\pi}
-\frac{it}{8}
\frac{\Log((b-ix)/(4\pi))}{b-ix}
+O\!\left(\frac1{|x|}\right)
+O_t\!\left(\frac{\log|x|}{x^2}\right).
\tag{12}
\]

The two load-bearing positive-frequency transforms are classical and can be checked by differentiating the Fourier transform of `(b-ix)^(-nu)` with respect to `b` or `nu`:

\[
\widehat{\Log(b-i\cdot)}(\xi)
=
-\frac{2\pi}{\xi}e^{-b\xi},
\qquad \xi>0,
\tag{13}
\]

and

\[
\widehat{\frac{\Log(b-i\cdot)}{b-i\cdot}}(\xi)
=
-2\pi e^{-b\xi}(\log\xi+\gamma),
\qquad \xi>0.
\tag{14}
\]

Replacing `Log(b-ix)` by `Log((b-ix)/(4 pi))` adds `log(4 pi)` to the bracket in (14). Multiplying by the carrier factor `(i/(2 pi))e^{a xi}` converts `e^{-b xi}` into `e^{-xi}`, because `b-a=1`. This proves the two singular terms in (6). The `O(1/x)` part of (12) contributes only bounded positive-frequency terms at the endpoint, while `O(log|x|/x^2)` is still milder. The coefficient in (6) is therefore independent of the auxiliary line height `a`, as it must be for consistency with the `a`-independence of the XF-051 carrier.

A useful sanity check is `t=0`: the first term of (6) has residue `-1/4`, exactly matching the explicit source normal form of XF-052,

\[
\mathcal Z_0(\xi)
=-\frac1{4\xi}+\frac74+O(\xi).
\]

The reference does not reproduce the entire regular Taylor series of XF-052 — nor should it, because `M_0` is a Stirling reference rather than the exact Xi factor — but it reproduces the only degree-`-1` endpoint component.

## 2. Why the bounded quotient is the right dynamic subtraction

The significant point of (5) is not merely that `H_t/B_t` stays bounded. Differentiating its logarithm forces a frequency factor `xi`. Thus the positive-time source naturally decomposes as

\[
\boxed{
\mathcal Z_t
=
\mathcal Z^M_t
+
\mathcal R_t,
\qquad
\mathcal R_t
=-\frac{\xi}{2\pi}e^{a\xi}\widehat L_{t,a}.
}
\tag{15}
\]

The deterministic reference carries the pole and the explicit heat-generated logarithmic cusp. The residual is already one endpoint derivative better. This suggests a cleaner version of the XF-088/XF-087 interface than repeatedly adding counterterms to the raw carrier: transport the reference analytically, and feed only the residual moments into the equal-weight/periodic construction.

This decomposition is also robust to root collisions and to hypothetical nonreal zeros. It uses only a zero-free horizontal line above the unconditional de Bruijn strip, exactly as XF-051 does; no labelled zero trajectories or simple-root hypothesis enters.

## 3. What this closes, and what it does not

The result closes one specific dynamic ambiguity left by XF-088. The logarithmic endpoint correction caused by the simple pole does **not** need to be re-estimated at every heat time. Its coefficient is fixed once and for all by the source residue `c=1/4`. In particular, a proposed continuum-to-grid theorem that produces a different leading `c_t log Delta` term for `t>0` is falsified by (5)--(8).

It does **not** yet prove the full positive-time trapezoid estimate. Boundedness of `L_{t,a}` alone is not an `X(B)` estimate for `\widehat L_{t,a}` on the shrinking guarded band, and it does not justify sampling the residual distribution pointwise. Further lower-order counterterms are not ruled out merely by the residue calculation. The live bridge is now sharper: prove that the residual in (15), or an equivalent reference quotient, has guarded source norm small enough for the XF-087 discretization and XF-086 equal-weight realization. The separate positive-transition coercivity gate also remains untouched.

The Polymath asymptotic is especially useful here because Proposition 9.1(ii) works on `3<=Im z<=4` without the `x>=exp(C/t)` threshold that appears in its sharper near-critical-line asymptotic. The high horizontal line is already legitimate for XF-051, and the carrier is independent of that line. Thus the pole-residue conclusion does not lose uniformity by sending `t downarrow 0`; the endpoint `t=0` is supplied exactly by XF-052.

## 4. Prior-art boundary and falsification controls

The load-bearing external input is D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn-Newman constant*, Research in the Mathematical Sciences 6 (2019), article 31, especially the explicit definitions of `M_t` and `alpha` and Proposition 9.1(ii). That paper is already anchored in `SOURCES.md`. It uses `M_t` as a high-line asymptotic/zero-free reference; the Fourier endpoint carrier and the residue statement (5)--(9) are derived here and are not attributed to the source. The Fourier transforms (13)--(14) are standard distributional identities.

A targeted literature search found no de Bruijn--Newman result formulating this high-line `M_t` quotient as a positive-frequency endpoint renormalization or identifying the resulting time-invariant `-1/4` carrier residue. No new source anchor is therefore required.

The strongest internal checks are structural. First, setting `t=0` recovers the XF-052 residue. Second, the auxiliary height cancels from every singular coefficient because the Fourier decay `e^{-(1+a)xi}` is multiplied by the XF-051 factor `e^{a xi}`. Third, the heat correction in (10) contains `alpha alpha'=O(log|x|/|x|)`, one full physical-space order below the leading `log|x|` term, so it cannot alter the `1/xi` coefficient even before using the bounded quotient. Finally, if the Polymath quotient were allowed to have logarithm growing linearly in `x`, the residual could in principle hide another pole; Proposition 9.1(ii) excludes exactly that failure mode on the chosen high line.

## 5. Consequence for `xi_flow`

XF-087 identifies the periodic low-mode dynamics as the exact trapezoidal discretization of the Volterra flow, and XF-088 shows that the source endpoint pole requires one logarithmic mesh counterterm. XF-089 now makes that counterterm dynamically stable:

\[
\boxed{
\text{the complete degree-`-1` endpoint sector is }
-\frac1{4\xi}
\text{ for every }0\le t\le\frac12.
}
\]

The remaining continuum-to-grid problem should therefore be formulated after **dynamic reference subtraction**, not as a fresh singular quadrature problem at each heat time. The next load-bearing estimate is a guarded Fourier-norm bound for the bounded quotient residual (15), sufficient to show that its continuum Volterra evolution and the periodic trapezoid remain `o(1)` apart on the `J<=m<=K` source band.