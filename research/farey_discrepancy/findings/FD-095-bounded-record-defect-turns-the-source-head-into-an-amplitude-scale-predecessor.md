# FD-095 — bounded record defect turns the source head into an amplitude-scale predecessor

**Status:** `EXACT-DERIVED + BOUNDED-RECORD-DEFECT + DYADIC-SOURCE-HEAD + SOURCE-LIPSCHITZ + FOUR-ADIC-BACKSTEP + FIXED-LOWER-OCCUPATION + DEFECT-INHERITANCE + ONE-STEP-CLOSURE`.

`FD-094` identifies backward normalized Schur-energy record defect as the entire fixed-occupation loss for every lower carrier that already has an exact nonsquarefree representation. It leaves one branch outside that mechanism: the row-two/source-head atom isolated by `FD-093`, because preserving the source value `mathcal H(B)` exactly on the smallest nonsquarefree row `4` returns to scale `4B=H+O(1)` rather than a genuine predecessor.

That exact-source obstruction disappears once one uses the unit increment law of the physical source instead of insisting on preserving the source argument literally. If the parent has bounded normalized-energy record defect, move the source argument **backward by any fixed fraction of its own amplitude** and reembed the nearby value on row `4`. The source changes by only that additive retreat, while the resulting physical horizon lies strictly below the parent. The same parent record defect then controls the complete lower denominator.

Consequently the source-head branch is not an independent composition gate. Under the same bounded-record-defect hypothesis already required by `FD-094`, it produces a genuinely lower sharp state with fixed nonsquarefree occupation and bounded inherited record defect. The remaining one-step composition gate is therefore only to couple a sharp occupied frontier packet to bounded normalized-energy record defect.

## 1. Setup: the terminal dyadic head and the normalized-energy defect

Retain the complete Schur energy and nonsquarefree energy

\[
E_{N,1}
=
\sum_{1<r\le N}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2,
\qquad
U_{N,1}
=
\sum_{\substack{1<r\le N\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2.
\tag{1}
\]

Fix `sigma>1/2` and, as in `FD-094`, write

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}},
\qquad
\mathfrak R_\sigma(H)
:=
\max\!\left\{
1,
\sup_{2\le N<H}
\frac{F_\sigma(N)}{F_\sigma(H)}
\right\}.
\tag{2}
\]

Suppose the sharp occupied packet at horizon `H` enters the dyadic terminal-head alternative of `FD-093`. Put

\[
A_2(H):=\left\lceil\frac H2\right\rceil,
\qquad
B_H:=\left\lfloor\frac{A_2(H)}2\right\rfloor,
\tag{3}
\]

so `B_H=H/4+O(1)`, and let

\[
S_H:=|\mathcal H(B_H)|.
\tag{4}
\]

The head alternative is

\[
\boxed{
S_H^2\ge\frac\eta6E_{H,1}
}
\tag{5}
\]

for the fixed parent occupation parameter `eta>0` carried by the frontier packet.

The exact source representation from `FD-033`/`FD-037` gives

\[
|\mathcal H(u)-\mathcal H(v)|\le |u-v|
\tag{6}
\]

for all nonnegative integers `u,v`. This elementary one-Lipschitz law is the extra input that was deliberately not used in the exact relabeling discussion of `FD-094`.

## 2. Back up by a fraction of the head amplitude and reembed on row four

Fix once and for all a real number

\[
0<\lambda<1.
\tag{7}
\]

For sufficiently large head episodes, `S_H` tends to infinity; choose

\[
h_H:=\lfloor\lambda S_H\rfloor,
\qquad
Y_H:=B_H-h_H,
\qquad
C_H:=4Y_H.
\tag{8}
\]

Because `mathcal H(0)=0` and (6) implies `S_H<=B_H`, one has

\[
Y_H\ge (1-\lambda)B_H-O(1)>0.
\tag{9}
\]

Moreover the floor geometry is completely explicit. For the four residue classes of `H` modulo `4`,

\[
H-4B_H\in\{-1,0,1,2\},
\tag{10}
\]

and hence

\[
\boxed{
H-C_H
=4h_H+O(1)
=4\lambda S_H+O(1).
}
\tag{11}
\]

In particular `C_H<H` as soon as `h_H>=1`. At the same time

\[
C_H\ge (1-\lambda)H-O(1),
\tag{12}
\]

so this is a genuine predecessor without leaving the parent power scale.

The source amplitude survives the retreat. By (6),

\[
|\mathcal H(Y_H)|
\ge S_H-h_H
=
(1-\lambda+o(1))S_H.
\tag{13}
\]

At horizon `C_H=4Y_H`, the nonsquarefree row `r=4` samples that value **exactly**:

\[
\left\lfloor\frac{C_H}{4}\right\rfloor=Y_H,
\qquad
w(4)=\frac{J_2(4)}{4^2}=\frac34.
\tag{14}
\]

Therefore

\[
\begin{aligned}
U_{C_H,1}
&\ge
\frac34|\mathcal H(Y_H)|^2\\
&\ge
\left(\frac34(1-\lambda)^2-o(1)\right)S_H^2\\
&\ge
\boxed{
\left(\frac\eta8(1-\lambda)^2-o(1)\right)E_{H,1}
}.
\end{aligned}
\tag{15}
\]

This is the missing lower physical carrier for the head branch. It is not obtained by preserving `mathcal H(B_H)` exactly; it is obtained by exploiting the source coherence that makes `mathcal H(B_H-h)` remain large over an amplitude-sized backward interval.

The minimal retreat `h_H=1` already works whenever `S_H>1` and gives the asymptotically stronger coefficient `eta/8-o(1)`, with `H-C_H` between `3` and `6`. The fixed-fraction choice (8) is more informative geometrically because it produces the amplitude-scale descent (11) while retaining a fixed share of the head energy.

## 3. Bounded parent record defect upgrades the backstep to fixed lower occupation

Assume now

\[
\mathfrak R_\sigma(H)\le K
\tag{16}
\]

for some fixed `K>=1`. Since `C_H<H`, definition (2) gives

\[
F_\sigma(C_H)
\le K F_\sigma(H),
\]

or equivalently

\[
E_{C_H,1}
\le
K\left(\frac{C_H}{H}\right)^{2\sigma}E_{H,1}.
\tag{17}
\]

Divide (15) by (17). The lower state has the fixed nonsquarefree occupation bound

\[
\boxed{
\frac{U_{C_H,1}}{E_{C_H,1}}
\ge
\left(
\frac{\eta(1-\lambda)^2}{8K}
-o(1)
\right)
\left(\frac H{C_H}\right)^{2\sigma}
\ge
\frac{\eta(1-\lambda)^2}{8K}-o(1).
}
\tag{18}
\]

Thus the row-two/source-head branch is repaired by the **same historical scalar** that controls the other branches in `FD-094`. No independent estimate on the row-two atom is required once the parent is within a fixed factor of its normalized-energy history.

The backstep also preserves normalized energy from below. Since `U_(C_H,1)<=E_(C_H,1)`, (15) gives

\[
\boxed{
F_\sigma(C_H)
\ge
\left(
\frac\eta8(1-\lambda)^2-o(1)
\right)
\left(\frac H{C_H}\right)^{2\sigma}
F_\sigma(H).
}
\tag{19}
\]

Consequently the predecessor itself inherits bounded backward defect. Every `N<C_H` is also `<H`, so

\[
\sup_{2\le N<C_H}F_\sigma(N)
\le K F_\sigma(H).
\]

Combining this with (19),

\[
\boxed{
\mathfrak R_\sigma(C_H)
\le
\frac{8K}{\eta(1-\lambda)^2}+o(1).
}
\tag{20}
\]

The constants may worsen, but they remain independent of `H`. Hence bounded record defect is a one-step hereditary property through the formerly terminal head branch.

## 4. Sharp false-RH scale is preserved and the head retreat is polynomially long

Suppose in addition that the parent belongs to a sharp false-RH frontier sequence,

\[
E_{H,1}=H^{2\Theta-o(1)},
\qquad
\Theta>\frac12.
\tag{21}
\]

Then (5) gives

\[
S_H\ge H^{\Theta-o(1)}.
\tag{22}
\]

Therefore the physical descent in (11) satisfies

\[
\boxed{
H-C_H\ge H^{\Theta-o(1)}.
}
\tag{23}
\]

for every fixed `lambda>0`, while (12) keeps `C_H` comparable to `H`. Equation (15) then yields

\[
E_{C_H,1}
\ge U_{C_H,1}
\gg_{\eta,\lambda} E_{H,1}
=H^{2\Theta-o(1)}
=C_H^{2\Theta-o(1)}.
\tag{24}
\]

The standard frontier upper envelope supplies the reverse exponent bound, so

\[
\boxed{
E_{C_H,1}=C_H^{2\Theta-o(1)},
\qquad
U_{C_H,1}\gg_{\eta,\lambda,K}E_{C_H,1}.
}
\tag{25}
\]

Thus a sharp occupied bounded-defect parent that falls into the source-head branch produces another **sharp, occupied, bounded-defect lower physical state**. The backstep is not merely a formal `C<H` perturbation; on a sharp frontier it moves by a polynomial additive distance at least `H^(Theta-o(1))`.

This does not yet justify indefinite recursion. The occupation and record-defect constants in (18) and (20) can deteriorate under repeated descent, and a long composition needs a uniform invariant or a re-recording mechanism that prevents that deterioration from accumulating. Equation (25) is a one-step closure theorem, not a completed infinite descent.

## 5. The two residual gates of `FD-094` collapse to one

For every repairable nonhead branch, `FD-094` already has a lower nonsquarefree mask `M_C` satisfying

\[
\frac{M_C}{C^{2\sigma}}
\ge(a-o(1))F_\sigma(H),
\qquad
M_C\le U_{C,1}\le E_{C,1},
\tag{26}
\]

with a fixed branch-dependent `a>0`. Besides the fixed occupation estimate stated there, (26) also immediately implies

\[
F_\sigma(C)\ge(a-o(1))F_\sigma(H)
\tag{27}
\]

and hence, whenever `mathfrak R_sigma(H)<=K`,

\[
\mathfrak R_\sigma(C)
\le\frac{K}{a-o(1)}.
\tag{28}
\]

Equations (18)--(20) show the same three properties for the only branch that `FD-094` excluded: lower physical scale, fixed nonsquarefree occupation, and bounded inherited normalized-energy defect.

Therefore the current repeated-prime predecessor theorem has the following **one-step closure principle**:

\[
\boxed{
\begin{array}{c}
\text{sharp occupied frontier state }H\\
+\ \mathfrak R_\sigma(H)=O(1)
\end{array}
\quad\Longrightarrow\quad
\begin{array}{c}
\text{some }C<H\text{ is sharp and occupied}\\
+\ \mathfrak R_\sigma(C)=O(1),
\end{array}
}
\tag{29}
\]

across the odd branch, the eligible dyadic branch, the dyadic nonhead repairs, **and the source-head branch**.

The conceptual consequence is that the head atom no longer needs a separate asymptotic exclusion theorem. The live first-order composition problem is singular: establish bounded `mathfrak R_sigma(H)` on at least one sufficiently sharp occupied packet sequence. If that gate is crossed, every current one-step branch has a lower fixed-occupation continuation.

A later multistep argument still has to control how the constants evolve under repeated applications of (29). In particular, an amplitude-scale head backstep is additive rather than a fixed-factor contraction when `Theta<1`, while odd-prime repairs may contract multiplicatively. The present result should therefore not be read as an infinite-descent contradiction.

## 6. Stress tests and prior-art boundary

The source one-Lipschitz law is essential. Without (6), moving from `B_H` to `B_H-h_H` could erase the head spike immediately and there would be no lower four-adic witness. Exact preservation of the source argument is deliberately abandoned; insisting on it recovers the `FD-093`/`FD-094` obstruction `4B_H=H+O(1)`.

The backward direction is also essential. Moving the source forward would generally place `4(B_H+h)` above `H`, where the parent backward record defect gives no denominator control. For the backward move, every destination `C_H` lies below `H` and is therefore priced by exactly the same `mathfrak R_sigma(H)` used in the repairable branches.

The fixed-fraction condition `lambda<1` prevents the retreat from consuming the entire source amplitude. Choosing `lambda` very close to one improves the physical descent but weakens the occupation constant by `(1-lambda)^2`; choosing `lambda` small does the opposite. No choice changes the qualitative conclusion as long as `lambda` is fixed independently of `H`.

A targeted prior-art audit covered recent Farey-discrepancy/Mertens work, record computations for the Mertens function, and GCD/Jordan-matrix literature. The located Farey work concerns local discrepancy and Mertens representations, current record work concerns computation of `M(x)`, and the GCD-matrix literature supplies general positivity/divisor structure. No located source states this Mathia-specific coupling of a dyadic source-head carrier, an amplitude-scale backward source move, four-adic reembedding, and a normalized Schur-energy record defect. No external theorem is load-bearing: the argument uses only the internal exact Jordan representation, the already-derived head inequality, the elementary unit increment law of `mathcal H`, and the definition of the backward record defect. `SOURCES.md` therefore requires no change.

The falsification boundary is explicit. If `mathfrak R_sigma(H)` diverges, (18) allows the lower occupation to vanish and the old composition problem returns. If the parent head amplitude is not frontier-sized, (23)--(25) do not follow. And although one step preserves boundedness of the defect, the constants can worsen from step to step; no uniform iterated bound is claimed. The durable gain is narrower but decisive for the present decomposition: **bounded normalized-energy record defect absorbs the source-head branch instead of leaving it as a second independent gate.**
