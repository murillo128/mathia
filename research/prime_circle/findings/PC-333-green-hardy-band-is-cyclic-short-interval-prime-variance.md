# PC-333 — Green-Hardy band is cyclic short-interval prime variance

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the band-uniform theorem target isolated in PC-332.

PC-332 reduces the surviving source-sensitive Green-Hardy question to the cumulative low-frequency estimate

\[
E_q(H):=\sum_{1\le h\le H}|e_q(h)|^2
\lesssim H\,\mu_q^{\mathrm{res}},
\tag{1}
\]

uniformly over a useful growing range, where `e_q` is the Fourier transform of the Li-subtracted prime source `d_q=p_q-w_q` from PC-330 and

\[
\mu_q^{\mathrm{res}}=\|d_q\|_2^2\sim \frac1{R_q}\sim\frac{\log q}{q}.
\tag{2}
\]

That target is not an autonomous new spectral condition. On the finite conductor circle it is, up to absolute constants and the reciprocal scale relation `H \asymp q/L`, equivalent to a moving-window mean-square bound for the same prime discrepancy. After undoing the probability normalization of the prime source, this is precisely the finite-cyclic analogue of the classical short-interval prime-variance/Selberg-integral problem.

The consequence is a novelty boundary, not a proof of (1): **proving the PC-332 band estimate by ordinary analytic-number-theory means would amount to proving a classical short-interval discrepancy estimate in Fourier coordinates.** A genuinely new prime-circle contribution must therefore be a geometry-forced proof, a stronger range or constant, or additional structure not already present in the classical variance problem.

## 1. Exact cyclic window identity

Work on `Z/qZ` and use the unnormalized Fourier transform

\[
\widehat d_q(h)
:=\sum_{x\bmod q}d_q(x)e^{-2\pi i hx/q}.
\tag{3}
\]

For an integer window length `1<=L<=q`, define the cyclic interval discrepancy

\[
S_{q,L}(x):=\sum_{j=0}^{L-1}d_q(x+j)
\tag{4}
\]

and its total mean square

\[
M_q(L):=\sum_{x\bmod q}|S_{q,L}(x)|^2.
\tag{5}
\]

Let

\[
D_L(h):=\sum_{j=0}^{L-1}e^{2\pi i hj/q}.
\tag{6}
\]

Finite cyclic Parseval gives the exact identity

\[
\boxed{
M_q(L)
=\frac1q\sum_{h\bmod q}
|\widehat d_q(h)|^2|D_L(h)|^2.
}
\tag{7}
\]

Because `d_q` has zero total mass, the zero mode vanishes. Thus the moving-window variance and the PC-332 Fourier-energy problem are two views of the same finite source, with the Dirichlet kernel selecting the reciprocal frequency scale.

## 2. Short-interval variance implies the PC-332 band bound

For `1<=h<=q/(2L)`,

\[
|D_L(h)|
=\left|\frac{\sin(\pi hL/q)}{\sin(\pi h/q)}\right|
\ge \frac{2L}{\pi}.
\tag{8}
\]

The residual is real, so

\[
|\widehat d_q(q-h)|=|\widehat d_q(h)|.
\tag{9}
\]

Therefore, with

\[
H:=\left\lfloor\frac{q}{2L}\right\rfloor,
\tag{10}
\]

(7)--(9) give

\[
M_q(L)
\ge
\frac{8L^2}{\pi^2q}
\sum_{1\le h\le H}|\widehat d_q(h)|^2,
\tag{11}
\]

hence

\[
\boxed{
E_q(H)
\le
\frac{\pi^2q}{8L^2}M_q(L).
}
\tag{12}
\]

Consequently a short-window mean-square estimate on the natural residual scale,

\[
M_q(L)\lesssim L\,\mu_q^{\mathrm{res}},
\tag{13}
\]

implies

\[
E_q(H)\lesssim H\,\mu_q^{\mathrm{res}}
\tag{14}
\]

at `H\asymp q/L`. Thus one direction of the PC-332 target is already exactly a short-interval variance statement after a reciprocal change of scale.

## 3. Uniform PC-332 band control implies short-interval variance

The converse holds, up to absolute constants, when (1) is available uniformly over the dyadic frequencies needed for the chosen window scale. For `|h|_q:=\min(h,q-h)`,

\[
|D_L(h)|
\ll
\min\!\left(L,\frac{q}{|h|_q}\right).
\tag{15}
\]

Take `2<=L<=q/2` and `H\asymp q/L`. Assume

\[
E_q(T)\le C T\mu_q^{\mathrm{res}}
\tag{16}
\]

for the relevant dyadic `T` between `H` and `q/2`. The low block contributes, before the factor `1/q` in (7),

\[
\ll L^2E_q(H)
\ll qL\mu_q^{\mathrm{res}}.
\tag{17}
\]

For a dyadic shell `T<h<=2T`, (15) and (16) give

\[
\sum_{T<h\le2T}
|\widehat d_q(h)|^2|D_L(h)|^2
\ll
\frac{q^2}{T^2}E_q(2T)
\ll
\frac{q^2}{T}\mu_q^{\mathrm{res}}.
\tag{18}
\]

With `T\asymp2^kq/L`, this is

\[
\ll 2^{-k}qL\mu_q^{\mathrm{res}}.
\tag{19}
\]

Summing the geometric tail, including the conjugate negative-frequency half, and restoring the factor `1/q` yields

\[
\boxed{
M_q(L)\lesssim L\mu_q^{\mathrm{res}}.
}
\tag{20}
\]

Hence, away from trivial endpoint effects, **uniform PC-332 spectral flatness and cyclic short-interval variance are equivalent up to absolute constants at reciprocal scales**. The extreme high-frequency endpoint is already controlled by total Parseval energy; the substantive content lies in the growing low/mesoscopic bands.

A Fejér-weighted version makes the same relation even more explicit. If

\[
F_q(H):=
\sum_{|h|<H}\left(1-\frac{|h|}{H}\right)
|\widehat d_q(h)|^2,
\tag{21}
\]

then hard and Fejér cutoffs control each other at neighboring scales by absolute constants. Thus the distinction between the PC-332 hard band and the standard smoothed Fourier concentration used for sliding sums is not structural.

## 4. Undoing normalization gives prime-count variance

PC-330 uses

\[
p_q(x)=\frac1{R_q}\mathbf1_{P_q}(x),
\qquad R_q=\pi(q)\sim\frac q{\log q},
\tag{22}
\]

with `w_q` the normalized Li-grid control. Therefore

\[
R_q S_{q,L}(x)
\tag{23}
\]

is the local prime count minus the matched normalized-Li prediction, modulo the deliberate cyclic wrapping and grid projection in the prime-circle model.

Using (2), the scale (20) becomes

\[
R_q^2 M_q(L)
\lesssim
L R_q,
\tag{24}
\]

and after averaging over the `q` starting points,

\[
\boxed{
\frac1q\sum_{x\bmod q}
|R_qS_{q,L}(x)|^2
\lesssim
\frac{L}{\log q}.
}
\tag{25}
\]

For polynomial mesoscopic scales this is the natural order of prime-count variance. The more refined classical formulations are usually written for `\psi` or `\Lambda` and carry the familiar scale-dependent logarithm, for example `h\log(X/h)` before dividing by the prime-weight `\log^2X`. Equation (25) should therefore be read as an order-of-magnitude cyclic analogue, not as an assertion that every normalization and endpoint range is identical to the continuous Selberg integral.

## 5. Prior-art audit: this analytic mechanism is classical

The Fourier-to-short-sum passage is classical analytic-number-theory technology. Gallagher's mean-square lemma for exponential sums is a standard bridge from frequency concentration to short sums; modern weighted versions explicitly formulate it in terms of Selberg integrals. A representative modern reference is G. Coppola and M. Laporta, *A generalization of Gallagher's lemma for exponential sums*, Šiauliai Mathematical Seminar 10(18) (2015), 29--47, arXiv:1411.1739.

More importantly for the RH-facing interpretation, D. A. Goldston and H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70, Birkhäuser (1987), 183--203, established under RH the classical equivalence between strong pair-correlation information for zeta zeros and second-moment statements for primes in short intervals. Tsz Ho Chan, *More Precise Pair Correlation of Zeros and Primes in Short Intervals*, J. London Math. Soc. 68 (2003), 579--598, DOI `10.1112/S0024610703004769`, develops sharper forms of the same equivalence. These references do not state the finite prime-circle normalization above verbatim; they establish that the substantive analytic bridge exposed by (7)--(25) already belongs to the classical short-interval/pair-correlation framework.

The exact finite-cyclic identities (7), (12), and the dyadic converse (20) are elementary harmonic analysis specialized here to the PC-330 residual. **Their role is a classicalization result:** they identify what the PC-332 theorem target really asks for, rather than supplying a new route around known prime-distribution difficulty.

## 6. Boundary and consequence for the research line

This finding does **not** say that the prime-circle Green construction is useless, nor that (1) cannot be proved geometrically. It says that the scalar band estimate itself cannot count as a new RH mechanism merely because it arose from a Green/Hilbert operator. Once the source is reduced to Fourier magnitudes, the remaining theorem is a classical prime-discrepancy variance problem in finite cyclic coordinates.

The live escape is consequently sharper. A substantive prime-circle advance would have to do at least one of the following: force (1) from an intrinsic geometric identity not already available in the classical short-interval theory; produce a materially stronger uniform range or asymptotic; retain phase/cross-level information discarded by the magnitude square; or connect the Green object to zeta zeros through additional structure rather than by importing the classical variance/pair-correlation bridge.

This also strengthens the information-loss warning already present in PC-325/PC-332. Any matched control with the same Fourier magnitudes has the same `E_q(H)`, the same Fejér energies, and therefore the same entire family of cyclic window variances. The scalar Green-Hardy route has reached a classical autocorrelation boundary; further progress must add information rather than repackage this variance.