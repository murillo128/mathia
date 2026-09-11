# MC-223 — Polylogarithmic character families cannot amortize a fixed-power exceptional sector

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-222` shows that GRH for Dirichlet `L`-functions closes the first square-defect shell by giving square-root-scale cancellation for every relevant Möbius progression. A natural weakening is to ask whether a zero-density or almost-all-character theorem could suffice: perhaps most character sectors are GRH-quality, while a sparse exceptional family is left with a weaker bound and becomes negligible after character averaging.

For the active first shell, **that relaxation cannot close the target through magnitude bounds alone**. The family is only polylogarithmically large, so character averaging supplies only `X^{o(1)}` dilution. Any single sector left at a fixed power above square-root scale can exceed the entire admissible budget unless its contribution is cancelled by phase interference or another source-coupled mechanism.

Keep the first-shell notation

\[
y=c\log X,
\qquad
q=\prod_{p\le y}p,
\qquad
T=X-q,
\qquad
y<d\le2y,\ d\ {m prime},
\]

and

\[
A_d(T)=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv-q\pmod{d^2}}}\mu(n).
\tag{1}
\]

Put

\[
\Phi_d:=\varphi(d^2)=d(d-1)=X^{o(1)}.
\tag{2}
\]

The exact character expansion from `MC-210`--`MC-222` is

\[
\boxed{
A_d(T)
=
\frac1{\Phi_d}
\sum_{\chi\ ({\rm mod}\ d^2)}
\overline{\chi(-q)}\,S_d(\chi),
}
\qquad
S_d(\chi)
:=
\sum_{\substack{n\le T\\(n,q)=1}}
\mu(n)\chi(n).
\tag{3}
\]

Suppose, for some fixed `delta>0`, that an argument divides the characters into a good set `G_d` and an exceptional set `E_d`, with

\[
|S_d(\chi)|\le X^{1/2+o(1)}
\quad(\chi\in G_d),
\tag{4}
\]

while the exceptional sectors are known only at the weaker fixed-power scale

\[
|S_d(\chi)|\le X^{1/2+\delta+o(1)}
\quad(\chi\in E_d).
\tag{5}
\]

Write `B_d=|E_d|`. If one uses no information about the relative phases of the exceptional terms, triangle inequality gives

\[
|A_d(T)|
\le
X^{1/2+o(1)}
+
\frac{B_d}{\Phi_d}X^{1/2+\delta+o(1)}.
\tag{6}
\]

Thus this magnitude-only certificate reaches the required square-root scale only when

\[
\boxed{
B_d
\le
\Phi_d X^{-\delta+o(1)}.
}
\tag{7}
\]

But `Phi_d=X^{o(1)}`. For every fixed `delta>0`, the right-hand side of `(7)` tends to zero. Hence, eventually,

\[
\boxed{B_d=0.}
\tag{8}
\]

In other words, **"all but a sparse exceptional set of characters" is not a useful fixed-power relaxation of the GRH-quality input for this proof interface**. A magnitude-only proof cannot leave even one character sector at `X^{1/2+delta}` for fixed `delta>0` and hope that the factor `1/Phi_d` absorbs it.

The same obstruction survives shell averaging. If a single exceptional sector of one modulus contributes with worst-case aligned phase and has size `X^{1/2+delta}`, its character-normalized contribution to the selected residue is of size

\[
\frac{X^{1/2+\delta}}{\Phi_d},
\]

so its possible contribution to the weighted first-shell energy is

\[
\boxed{
 d\left(\frac{X^{1/2+\delta}}{\Phi_d}\right)^2
=
X^{1+2\delta-o(1)},
}
\tag{9}
\]

because `d,\Phi_d=X^{o(1)}`. This is polynomially above the target

\[
W_y(X)
:=
\sum_{y<d\le2y\atop d\ {m prime}}
 d|A_d(T)|^2
\le X^{1+o(1)}.
\tag{10}
\]

Equation `(9)` is a worst-case certification barrier, not a lower bound for the actual Möbius contribution: the exceptional sector may in reality cancel against other sectors. That distinction is exactly the point. **Sparsity of exceptional sectors is powerless at fixed-power resolution unless the proof also controls their signed aggregate.**

No estimate for `A_d`, `W_y`, `M(X)`, or any Dirichlet zero set is proved here.

## 1. The exact exceptional-sector budget

More generally, suppose every exceptional sector is bounded by

\[
|S_d(\chi)|\le X^{\beta+o(1)},
\qquad \beta\ge\frac12.
\tag{11}
\]

The exceptional part of the triangle certificate is

\[
\frac1{\Phi_d}
\sum_{\chi\in E_d}|S_d(\chi)|
\le
\frac{B_d}{\Phi_d}X^{\beta+o(1)}.
\tag{12}
\]

Therefore a magnitude-only proof can certify `X^{1/2+o(1)}` only if

\[
\boxed{
B_d
\le
\Phi_d X^{1/2-\beta+o(1)}.
}
\tag{13}
\]

This gives a useful near-critical calibration. If there is just one exceptional character, `(13)` can tolerate only

\[
X^{\beta-1/2}\le\Phi_d X^{o(1)}.
\tag{14}
\]

Since `d\asymp\log X` and `Phi_d\asymp(\log X)^2`, a single uncontrolled sector may exceed square-root only by a polylogarithmic factor. In exponent language, the admissible excess satisfies at most

\[
\beta-\frac12
\le
\frac{(2+o(1))\log\log X}{\log X}
\tag{15}
\]

before the explicit `Phi_d` dilution is exhausted. There is **no fixed positive exponent margin**.

A Cauchy/Parseval treatment does not rescue a fixed-power exceptional sector. From `(3)`,

\[
|A_d(T)|^2
\le
\frac1{\Phi_d}
\sum_{\chi\ ({\rm mod}\ d^2)}|S_d(\chi)|^2.
\tag{16}
\]

If `B_d` sectors are bounded only by `X^beta`, their worst-case contribution to `(16)` is

\[
\frac{B_d}{\Phi_d}X^{2\beta+o(1)}.
\tag{17}
\]

Keeping this at `X^{1+o(1)}` requires

\[
B_d\le\Phi_d X^{1-2\beta+o(1)},
\tag{18}
\]

which again forces `B_d=0` for every fixed `beta>1/2`. The triangle estimate is actually the less expensive magnitude-only certificate when the exceptional set is small; both have the same fixed-power conclusion.

## 2. Why family sparsity works in the wrong direction here

The shell contains only

\[
\pi(2y)-\pi(y)=X^{o(1)}
\]

moduli, and each modulus has only

\[
\Phi_d=X^{o(1)}
\]

characters. Thus the entire character family visible to the first shell has cardinality `X^{o(1)}`.

That sounds favorable for a family argument, but at the power scale it removes the usual amortization mechanism. A density theorem can make the **number** of bad sectors very small relative to a large family; here even one fixed-power bad sector remains polynomially visible after every available counting normalization. A proof that only says "all but `o(Phi_d)` characters are good" can therefore be much too weak: `o(Phi_d)` may still contain one character, while `(7)` demands eventual emptiness when the residual bound is `X^{1/2+delta}`.

This statement concerns what follows from count-plus-magnitude information. It does not assert that a zero off the critical line necessarily produces a twisted sum of the extremal size in `(5)`, and it does not turn a zero-density theorem into a theorem about `S_d(chi)`. Even **granting** such a good/bad reduction, density alone would not close the selected-residue target through absolute values.

## 3. The surviving theorem surface is signed exceptional-sector energy

The obstruction identifies precisely what an almost-all or zero-density input would still need to supply. Define the exceptional signed coordinate

\[
C_d(E_d)
:=
\frac1{\Phi_d}
\sum_{\chi\in E_d}
\overline{\chi(-q)}S_d(\chi).
\tag{19}
\]

If the good sectors satisfy `(4)`, then a sufficient shell-level replacement for uniform GRH-quality control is

\[
\boxed{
\sum_{y<d\le2y\atop d\ {m prime}}
 d\,|C_d(E_d)|^2
\le X^{1+o(1)}.
}
\tag{20}
\]

Unlike `B_d`, the quantity `(20)` retains the relative phases and the source-selected coordinate. It allows individual exceptional sectors to be large provided they cancel in the exact linear combination seen by the square-defect source.

By `MC-215`, the displayed factors `chi(-q)` are themselves removable by a residue-coordinate gauge, so `(20)` should not be read as a request for a lucky explicit phase identity. The invariant content is cancellation of the **translated exceptional coefficient vector at the distinguished coordinate**, or an equivalent cross-modulus/lifted statement retaining `n+q=d^2m`.

This converts the post-`MC-222` question into a sharper dichotomy:

1. obtain essentially uniform square-root control for every character sector, which is naturally GRH-strength by the sectorwise reciprocal-`L` route; or
2. prove a signed aggregate estimate such as `(20)` that neutralizes the exceptional sectors without controlling them individually.

A density count without such a signed aggregate lies strictly between those two interfaces and does not close the power budget.

## 4. Prior-art audit

Halupczok and Suger, *Partial sums of the Möbius function in arithmetic progressions assuming GRH* (arXiv:1111.3305; Functiones et Approximatio 48 (2013), 61--90), provide the uniform GRH-conditional progression estimate used in `MC-222`. Their result is the positive endpoint of the dichotomy above: every relevant progression is controlled at square-root scale up to subpower factors.

Corrigan and Zhao, *Zero-Density Theorems for Families of Dirichlet L-functions* (arXiv:2211.00260; Bulletin of the Australian Mathematical Society 108 (2023), 224--235), prove zero-density estimates for families including characters with moduli from sparse sets and of fixed orders. Dickinson, *Zeros of Dirichlet L-functions near the critical line* (arXiv:2211.06264; Mathematika 70 (2024)), proves density bounds close to the critical line using twisted second moments. These works confirm that density control for Dirichlet families is a genuine and developed alternative to uniform GRH, including sparse-family settings.

They do **not** directly state the good/bad twisted-Möbius hypothesis `(4)`--`(5)`, and this finding does not attribute such a consequence to them. Their role is to audit the natural proposal "replace GRH by a density theorem". The calculation `(13)` shows that even an idealized translation of density information into square-root control for almost all sectors would still leave a fixed-power gap unless the exceptional sectors are either individually near-square-root or cancelled in the signed source coordinate.

The inequalities `(6)`--`(18)` are elementary character-orthogonality bookkeeping, not claimed as new analytic-number-theory theorems. The durable line-specific result is the **power-budget diagnosis for the exact first square-defect shell**: its polylogarithmic character family is too small to absorb even one fixed-power exceptional sector by cardinality alone.

## 5. Falsification boundaries

- `(7)` and `(13)` are requirements for a **magnitude-only certificate**, not necessary conditions for the actual Möbius sum. Character phases can cancel, and `(20)` records exactly that escape.
- No implication from a Dirichlet zero to a particular lower bound for `|S_d(chi)|` is asserted. Zero-density literature is used only as adjacent prior art for family sparsity, not as a hidden converse theorem.
- A polylogarithmic excess above `X^(1/2)` is compatible with the explicit `Phi_d` dilution. The obstruction is specifically to a fixed exponent `1/2+delta` with `delta>0` independent of `X`.
- The argument is specialized to the first shell `d\asymp log X`. Larger square-defect shells have different family sizes and must redo the exponent budget rather than importing `(8)` unchanged.
- A theorem giving cancellation across exceptional characters, across moduli, or through the lifted relation `n+q=d^2m` is not excluded. Such a theorem is precisely the remaining target.

## Consequence for the live frontier

After `MC-222`, **generic zero-density is not the next theorem surface by itself**. The useful question is whether exceptional Dirichlet sectors, if they exist, have a source-forced signed aggregate satisfying `(20)`. This is narrower than proving GRH for the whole family and stronger than counting exceptional sectors. It points directly back to the only information that the characterwise route discards: principal/transverse interference, cross-modulus coherence, and the integer lift tying every selected residue to the same primorial source.