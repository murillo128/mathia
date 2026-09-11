# MC-209 — Square-defect level doubling can be replaced by a dyadic Möbius-variance target

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CANDIDATE-NEW-STRUCTURE`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-208` shows that the primorial-shift square-defect transform

\[
\Delta(X;y)
=-\sum_{\substack{d>y\\(d,q)=1\\d^2\le X}}\mu(d)A_d(T),
\qquad
A_d(T)
:=\sum_{\substack{n\le T\\(n,q)=1\\n\equiv-q\pmod{d^2}}}\mu(n),
\tag{1}
\]

with

\[
q=\prod_{p\le y}p,
\qquad y=c\log X,
\qquad T=X-q,
\tag{2}
\]

pays a level-doubling penalty if the large-`d` tail is discarded by absolute values: progression control through `d\le D` only controls square moduli through `d^2\le D^2`, while the remaining absolute tail is `O(X/D+\sqrt X)`. The same transform has a second exact organization which does **not** require a pointwise or uniform estimate for each fixed-`m` cubic polynomial from `MC-208`.

For a dyadic root-modulus shell

\[
\mathcal D(D)
:=\{d:D<d\le2D,\ (d,q)=1,\ d^2\le X\},
\tag{3}
\]

put

\[
\Delta_D
:=-\sum_{d\in\mathcal D(D)}\mu(d)A_d(T)
\tag{4}
\]

and define the weighted prescribed-residue energy

\[
\boxed{
V_D
:=\sum_{d\in\mathcal D(D)}d\,|A_d(T)|^2.
}
\tag{5}
\]

Then Cauchy--Schwarz gives the exact shell estimate

\[
\boxed{
|\Delta_D|^2
\le
\left(\sum_{d\in\mathcal D(D)}\frac1d\right)V_D
\ll V_D.
}
\tag{6}
\]

Consequently the family of bounds

\[
\boxed{
V_D\ll_\varepsilon X^{1+\varepsilon}
}
\tag{7}
\]

uniformly for the `O(log X)` dyadic shells `y\le D\le\sqrt X` would imply

\[
\boxed{
\Delta(X;y)\ll_\varepsilon X^{1/2+\varepsilon}.
}
\tag{8}
\]

The scale in `(7)` is not arbitrary. After reparametrizing the progression by

\[
n=d^2r-q,
\tag{9}
\]

one has, because `(d,q)=1`,

\[
\boxed{
A_d(T)
=
\sum_{\substack{q/d^2<r\le X/d^2\\(r,q)=1}}
\mu(d^2r-q).
}
\tag{10}
\]

Expanding the square in `(5)` separates a diagonal contribution and a structured two-point correlation family. The diagonal is already at the desired scale **without any Möbius cancellation**:

\[
V_D^{\rm diag}
:=
\sum_{d\in\mathcal D(D)}d
\sum_{\substack{q/d^2<r\le X/d^2\\(r,q)=1}}
\mu^2(d^2r-q)
\ll
X+D^2
\ll X.
\tag{11}
\]

The entire excess over the diagonal is therefore

\[
\boxed{
V_D^{\rm off}
=
\sum_{d\in\mathcal D(D)}d
\sum_{\substack{h\ne0\\|h|\ll X/d^2}}
\sum_{r\in I_d\cap(I_d-h)}
\mathbf 1_{(r(r+h),q)=1}
\mu(d^2r-q)\mu(d^2(r+h)-q),
}
\tag{12}
\]

where `I_d=(q/d^2,X/d^2]`. Thus `(7)` asks for the **aggregate off-diagonal two-point Möbius correlation to remain at diagonal scale**. It does not ask for Chowla cancellation separately for every shift, every modulus, or every fixed polynomial from `MC-208`.

This changes the live frontier in a useful way. The `MC-208` dual tail

\[
\sum_m\sum_d\mu(d)\mu(md^2-q)
\tag{13}
\]

looks, after freezing `m`, like Möbius evaluated on the reducible cubic `d(md^2-q)`, placing a pointwise attack in polynomial-Chowla territory. The energy representation `(12)` instead freezes `d` and squares the corresponding square-modulus progression sum. The missing statement becomes a **Barban--Davenport--Halberstam / averaged-Chowla type variance problem on one source-prescribed reduced residue per square modulus**.

No bound of the form `(7)` is proved here. No improved estimate for `M(X)`, `A_d`, `\Delta`, or the zeta zero set is claimed. The result is an exact reduction identifying an alternative theorem surface that avoids throwing away the large-`d` tail by absolute values.

## 1. The dyadic Cauchy reduction removes the absolute tail split

From `(4)`,

\[
|\Delta_D|
\le
\left(\sum_{d\in\mathcal D(D)}\frac1d\right)^{1/2}
\left(\sum_{d\in\mathcal D(D)}d|A_d(T)|^2\right)^{1/2}.
\tag{14}
\]

Since `D<d\le2D`,

\[
\sum_{d\in\mathcal D(D)}\frac1d\le\sum_{D<d\le2D}\frac1d\ll1,
\tag{15}
\]

which proves `(6)`. Summing `(6)` over at most `O(log X)` dyadic shells and absorbing logarithms into `X^\varepsilon` proves `(8)` from `(7)`.

The key distinction from `MC-208` is structural. There is no cutoff `D` after which each `|A_d|` is replaced by its progression length. Every root modulus remains present, but only through a second moment. The price is that `(7)` is itself a serious Möbius-variance theorem rather than a consequence of support sparsity.

## 2. The target energy has the natural diagonal size

Equation `(10)` follows because

\[
n\equiv-q\pmod{d^2}
\quad\Longleftrightarrow\quad
n=d^2r-q,
\tag{16}
\]

and

\[
(d^2r-q,q)=(r,q)
\tag{17}
\]

when `(d,q)=1`. The upper condition `n\le X-q` is exactly `r\le X/d^2`.

Expanding `|A_d|^2` and separating `r=s` from `r\ne s` gives `(11)`--`(12)`. For the diagonal, `|mu|^2\le1`, so

\[
V_D^{\rm diag}
\le
\sum_{D<d\le2D}d\left(\frac{X}{d^2}+1\right)
\ll
X\sum_{D<d\le2D}\frac1d
+
\sum_{D<d\le2D}d
\ll X+D^2.
\tag{18}
\]

Since the shell is nonempty only for `D\ll\sqrt X`, `(11)` follows.

For comparison, discarding all sign cancellation before squaring gives

\[
V_D
\ll
\sum_{D<d\le2D}d\left(\frac{X}{d^2}+1\right)^2
\ll
\frac{X^2}{D^2}+X+D^2.
\tag{19}
\]

At the `MC-208` transition `D=X^{1/4}`, `(19)` is `O(X^{3/2})`, whereas the diagonal target `(7)` is `X^{1+o(1)}`. The missing factor `X^{1/2}` is exactly the scale of cancellation that the absolute-tail treatment loses there. Near `D=\sqrt X`, the diagonal scale is already trivial; the real difficulty is spread over the lower and intermediate square-modulus shells.

This makes `(7)` falsifiable and quantitatively calibrated: a proof need not manufacture an unexpectedly tiny variance, only prevent coherent off-diagonal correlations from accumulating polynomially above the diagonal scale.

## 3. The off-diagonal is averaged two-point Chowla with square dilation

For `s=r+h`, the two Möbius arguments in the off-diagonal expansion are

\[
L_{d,0}(r)=d^2r-q,
\qquad
L_{d,h}(r)=d^2(r+h)-q,
\tag{20}
\]

whose difference is `h d^2`. Hence `(12)` is a weighted average of two-point correlations along pairs of parallel linear forms, with three coupled features:

1. the common leading coefficient is the square `d^2`;
2. the shift is simultaneously constrained to be a multiple `h d^2`;
3. the primorial pre-sieve requires `(r(r+h),q)=1`.

Those couplings are load-bearing. Ordinary averaged Chowla for

\[
\sum_{n\le X}\mu(n)\mu(n+h)
\tag{21}
\]

averaged over unrestricted `h` does not directly imply `(7)`, because `(12)` samples one residue class modulo each `d^2` and ties the shift to that same square modulus. Conversely, `(7)` does not require uniform cancellation for each individual `(d,h)` pair: cancellations may occur across `h`, across `d`, or internally in the progression sums before the shell energy is formed.

This is a strictly different proof interface from trying to establish, uniformly in `m`, cancellation of

\[
\sum_d\mu\!\left(d(md^2-q)\right)
\tag{22}
\]

from `MC-208`. Neither interface is asserted to be logically weaker in every parameter regime, but `(7)` exposes averaging that `(22)` suppresses.

## 4. Prior-art audit: square-modulus variance exists, but not this Möbius target

Several established theories sit immediately adjacent to `(7)`.

Matomäki, Radziwiłł and Tao, *An averaged form of Chowla's conjecture*, Algebra & Number Theory 9 (2015), 2167--2196, prove qualitative cancellation of fixed-order Möbius correlations after averaging over ordinary shifts `h\le H` with `H\to\infty`. This is already recorded as `MC-S13`. It confirms that averaging over shifts can cross a barrier that is inaccessible shift-by-shift, but it does not include the square-modulus/residue coupling in `(12)`.

Stephan Baier and Liangyi Zhao, *Bombieri--Vinogradov type theorems for sparse sets of moduli*, Acta Arithmetica 125 (2006), 187--201, DOI `10.4064/aa125-2-5`, prove both Barban--Davenport--Halberstam and Bombieri--Vinogradov type theorems for sparse moduli. Their Theorem 2 treats **square moduli** and reaches root moduli `d\le x^{1/2-\varepsilon}` in a weighted mean-square theorem for the prime-counting error; their Theorem 4 gives a Bombieri--Vinogradov type result for square root moduli `d\le x^{2/9-\varepsilon}`. These are results for `Lambda` with its prime main term removed, not estimates for the prescribed-residue Möbius sums `(10)`. They nevertheless show that the squaring `d\mapsto d^2` is not by itself an absolute prohibition on deep mean-square averaging.

Stephan Baier, *The large sieve for square moduli, revisited*, arXiv:2503.18009 (2025), reviews the generic square-modulus large-sieve state of the art. In his notation the best unconditional bound from Baier--Zhao (2008) has large-sieve constant

\[
(QN)^\varepsilon
\left(Q^3+N+\min\{Q^2N^{1/2},Q^{1/2}N\}\right),
\tag{23}
\]

and the critical point `Q=N^{1/3}` remains a factor `Q^{1/2}` above the conjectural `Q^3+N` scale; the 2025 paper obtains improvements only conditionally on higher additive-energy hypotheses for modular square roots. This controls an all-fractions Fourier norm for arbitrary coefficient sequences. It does not by itself yield the source-specific energy `(5)`, whose coefficient sequence is Möbius and whose residue is fixed as `-q mod d^2`.

Jonathan Keating and Zeev Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, Algebra & Number Theory 10 (2016), 375--420, already recorded as `MC-S44`, calculate Möbius progression variances in the function-field analogue. Their result supports variance as a natural object and a useful model, but it does not provide an integer theorem of the strength `(7)`.

A targeted literature search also finds GRH-conditional pointwise work on Mertens sums in arithmetic progressions (Karin Halupczok and Benjamin Suger, arXiv:1111.3305) and modern general Barban--Davenport--Halberstam frameworks for suitable sequences, but no theorem identified in this audit directly supplies `(7)` for the growing primorial source, one prescribed reduced residue per square modulus, and the full dyadic range. No literature-absence claim is made.

The elementary Cauchy reduction `(6)` and diagonal calculation `(11)` are not claimed as standalone novelty. The durable contribution is the line-specific synthesis: **the level-doubling branch can be attacked by proving diagonal-scale dyadic variance instead of extending pointwise progression control to near-level one or proving a uniform polynomial-Chowla theorem.**

## 5. Falsification boundaries and next theorem surface

The variance route survives only if its hypotheses remain independently weaker than the desired Mertens conclusion.

- A bound for `V_D` obtained by first assuming RH/GRH-quality cancellation for every `A_d` is circular for the purpose of this line; it verifies the implication but supplies no mechanism.
- Replacing `(5)` by an all-residue variance can be much stronger than necessary. The target uses exactly one residue `-q mod d^2`, selected by the square-defect identity.
- Centering `A_d` by an unproved Möbius main term must not hide the principal cancellation problem. The uncentered energy `(5)` is the safe target.
- Generic square-modulus large-sieve estimates for arbitrary coefficients should not be advertised as proving `(7)` unless the conversion to the prescribed residue, imprimitive frequencies, and primorial pre-sieve is carried out with the required `X^{1+o(1)}` budget.
- Ordinary averaged Chowla cannot be imported without controlling the coupling `shift = h d^2` and the simultaneous residue condition `n\equiv-q mod d^2`.
- A finite numerical observation that `V_D` is near `X` is only heuristic. The theorem surface is a uniform analytic estimate through the required dyadic range.

A decisive positive result for this branch is therefore an unconditional estimate

\[
V_D\ll X^{1+o(1)}
\tag{24}
\]

for all or a sufficiently complete family of dyadic root-modulus shells, derived from arithmetic information not already equivalent to Mertens square-root cancellation. A useful partial result would prove `(24)` on a new range of `D` and quantify exactly how the uncovered shells feed back through `(6)`. A decisive negative result would show that a natural matched multiplicative source satisfies the available progression/averaged-Chowla inputs but has `V_D` polynomially above the diagonal scale, demonstrating that those inputs cannot control the square-defect transform.