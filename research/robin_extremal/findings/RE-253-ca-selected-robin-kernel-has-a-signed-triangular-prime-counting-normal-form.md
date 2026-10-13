# RE-253 — CA-selected Robin kernel has a signed triangular prime-counting normal form

**Status:** EXACT-DERIVED + SOURCE-SELECTED-LOCAL-REDUCTION + LITERATURE-COROLLARY + PRIOR-ART-BOUNDED; independent adversarial review pending.

**Dependencies:** RE-021 (ordinary-prime endpoint at every regular self-tangent CA state), RE-022 (exact mixed-race height/tail identity), RE-252 (Guth–Maynard pointwise short-interval input and near-border window).

RE-252 proves that the first piece of the ordinary-prime mixed-race integral is negligible up to a stretched-exponentially enlarged frontier, but its pointwise short-interval estimate stops giving \(o(1)\) at the error-balance horizon \(H_\star\). The direct local integral has a more informative *signed* reduction: its leading contribution is the first integral, or triangular/Riesz mean, of the ordinary-prime counting discrepancy. This states exactly what additional cancellation would be needed at that frontier, without claiming that it occurs.

## Precise local theorem

For any sufficiently large **ordinary prime** \(p\), write \(L=\log p\), \(\Delta(t)=\vartheta(t)-t\), and retain the exact Robin functions
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\qquad
k(t)=\frac1{t\log t},\qquad
I(t)=\Delta(t)h'(t)-\bigl(h(t)-k(t)\bigr).
\]
Define, for \(H\ge0\),
\[
N_p(y)=\pi(p+y)-\pi(p),\qquad
D_p(H)=\int_0^H\left(N_p(y)-\frac yL\right)\,dy
=\sum_{p<q\le p+H}\bigl(H-(q-p)\bigr)-\frac{H^2}{2L},
\tag{1}
\]
where \(q\) ranges over ordinary primes; the endpoint term at \(q=p+H\) is zero. Put
\[
a_p=-\sqrt p\,L^2h'(p)
=\sqrt p\left(\frac{L}{p(p-1)}
+\frac{-\log(1-p^{-1})}{p}\right)
=\frac{L}{p^{3/2}}\left(1+O(L^{-1})\right)>0.
\tag{2}
\]

**Theorem (unconditional signed local normal form).** Uniformly for *every* ordinary prime \(p\) sufficiently large and every real \(1\le H\le p/2\),
\[
\boxed{
\sqrt p\,L\int_p^{p+H}I(t)\,dt
=-a_p D_p(H)
+O\left(
\frac{H(1+|\Delta(p)|)}{p^{3/2}}
+\frac{L H^3}{p^{5/2}}
\right).
}
\tag{3}
\]
The constant is absolute. The selected-prime hypothesis is **not** used to derive (3); it controls the size of its explicit endpoint remainder.

When \(p\) is the last active first-layer prime of a sufficiently large **regular self-tangent colossally abundant integer** \(C\), RE-021 gives \(|\Delta(p)|\ll p^{0.52}\). Consequently for each fixed \(0<\varepsilon<1/6\), (3) becomes
\[
\sqrt p\,L\int_p^{p+H}I(t)\,dt
=-a_p D_p(H)+O_\varepsilon(p^{-c_\varepsilon}),
\qquad
1\le H\le p^{5/6-\varepsilon},
\tag{4}
\]
with, for example, any fixed \(c_\varepsilon<\min\{1/10,2\varepsilon\}\). Equation (4) is a **power-saving absolute approximation**, not an assertion that the prime-counting moment or the integral is small.

## Derivation and error audit

For \(0\le y\le p/2\), decompose the exact Chebyshev increment:
\[
\begin{aligned}
\Delta(p+y)
&=\Delta(p)+\sum_{p<q\le p+y}\log q-y\\
&=\Delta(p)+L\left(N_p(y)-\frac yL\right)+S_p(y),\\
S_p(y)&:=\sum_{p<q\le p+y}\log(q/p).
\end{aligned}
\tag{5}
\]
Because \(0\le\log(q/p)\le(q-p)/p\le y/p\), while \(N_p(y)\le y+1\) by the trivial integer-count bound,
\[
0\le S_p(y)\le y(y+1)/p,\qquad
\left|N_p(y)-y/L\right|\ll y+1.
\tag{6}
\]
No prime-number theorem is required for these inequalities.

On the entire interval \(p\le t\le3p/2\), direct differentiation of \(h\) and the positive logarithm series yield
\[
|h'(t)|\ll(p^2L)^{-1},\quad
|h''(t)|\ll(p^3L)^{-1},\quad
0<h(t)-k(t)\ll(p^2L)^{-1}.
\tag{7}
\]
Hence \(h'(p+y)=h'(p)+O(y/(p^3L))\). Substitute (5) in the kernel and freeze \(h'\) at \(p\):
\[
\begin{aligned}
\sqrt pL\int_p^{p+H}I(t)\,dt
&=\sqrt pL^2h'(p)D_p(H)
+\sqrt pL h'(p)H\Delta(p)\\
&\quad+\sqrt pL h'(p)\int_0^H S_p(y)\,dy\\
&\quad+\sqrt pL\int_0^H
\Delta(p+y)\bigl(h'(p+y)-h'(p)\bigr)\,dy\\
&\quad-\sqrt pL\int_p^{p+H}(h(t)-k(t))\,dt.
\end{aligned}
\tag{8}
\]
The first term is exactly \(-a_pD_p(H)\). Equations (6)–(7) bound the other four respectively by
\[
O\left(\frac{H|\Delta(p)|}{p^{3/2}}\right),\quad
O\left(\frac{H^3+H^2}{p^{5/2}}\right),\quad
O\left(\frac{H^2|\Delta(p)|+L(H^3+H^2)}{p^{5/2}}\right),\quad
O\left(\frac H{p^{3/2}}\right).
\tag{9}
\]
Use \(1\le H\le p/2\) to absorb \(H^2|\Delta(p)|/p^{5/2}\) into \(H|\Delta(p)|/p^{3/2}\), and \(H^2\le H^3\). This proves (3). The selected-endpoint estimate and \(H\le p^{5/6-\varepsilon}\) give the stated power saving in (4); the endpoint term is at most \(p^{-0.146\ldots-\varepsilon}\), while the cubic term is at most \(Lp^{-3\varepsilon}\).

## The Guth–Maynard error-balance window is equivalent to a signed prime-counting moment

Use RE-252's exact horizon
\[
H_\star(p)=\frac{p^{3/4}}{\sqrt L}\exp\left(\frac12 L^{1/4}\right).
\tag{10}
\]
For every selected \(p\) as above, the remainder in (3) is \(O(p^{-1/5})\), uniformly for \(0\le H\le H_\star\) (the \(H<1\) case follows from the same estimates without division by \(H\)). Thus
\[
\boxed{
\sqrt pL\int_p^{p+H} I(t)\,dt
=-a_pD_p(H)+O(p^{-1/5})
\qquad(0\le H\le H_\star).
}
\tag{11}
\]

Guth–Maynard's *pointwise* Corollary 1.3, as applied in RE-252 with \(\varepsilon=1/30\), gives
\[
N_p(y)-y/L=O\!\left(y e^{-L^{1/4}}\right)
\qquad(p^{3/5}\le y\le H_\star).
\tag{12}
\]
Below \(p^{3/5}\) use (6). Integration yields, uniformly for \(H\le H_\star\),
\[
|D_p(H)|\ll p^{6/5}+H^2e^{-L^{1/4}}
\ll \frac{p^{3/2}}L.
\tag{13}
\]
Since \(a_p=L p^{-3/2}+O(p^{-3/2})\), (11) and (13) also give
\[
\boxed{
\sqrt pL\int_p^{p+H}I(t)\,dt
=-\frac L{p^{3/2}}D_p(H)+O(L^{-1}+p^{-1/5}),
\quad 0\le H\le H_\star.
}
\tag{14}
\]
In particular, **along any unbounded selected-prime sequence**, the following are equivalent:
\[
\boxed{
\sqrt pL\int_p^{p+H_\star(p)}I(t)\,dt=o(1)
\quad\Longleftrightarrow\quad
D_p(H_\star(p))=o(p^{3/2}/L).
}
\tag{15}
\]
The analogous *uniform* invisibility criterion on the entire interval \([0,H_\star]\) replaces the moment on the right by
\(\sup_{0\le H\le H_\star}|D_p(H)|=o(p^{3/2}/L)\).
The pointwise Guth–Maynard estimate gives only the corresponding \(O\)-bound, **not** this little-\(o\) statement. The new condition identifies precisely the missing *signed cancellation* at the error-balance scale; it does not establish it.

Finally, combining (11) with RE-022's remote PNT truncation and RE-021's CA tax gives, for each fixed \(A>A_0\),
\[
\begin{aligned}
\sqrt pL\bigl(\log G(C)-\gamma\bigr)
&=-a_pD_p(H_\star)
+\sqrt pL\int_{p+H_\star}^{U_A(p)}I(t)\,dt\\
&\quad-2\sqrt2
+\frac{\sqrt2(2+\log2)}L+O_A(L^{-2}).
\end{aligned}
\tag{16}
\]
Unlike the invisible cutoff \(H_{\rm near}=H_\star e^{-L^{1/8}}\) of RE-252, (16) retains an explicit, potentially order-one local correction at the actual error-balance horizon.

## Prior art, falsification and boundaries

Triangular prime-counting sums, integrated counting discrepancies, and their first-order Riesz/Cesàro smoothing are **classical constructions**, not newly discovered arithmetic statistics. The pointwise short-interval theorem is Guth and Maynard, *New large value estimates for Dirichlet polynomials*, *Annals of Mathematics* **203** (2026), 623–675, Corollary 1.3, DOI 10.4007/annals.2026.203.2.6. The exact CA selector and mixed Robin kernel were already established in RE-021–RE-022; RE-252 supplies the sharp available pointwise error scale. A targeted search against prime-counting short-interval/Riesz-mean and divisor-sum/Robin sources did not locate this specific selected-kernel reduction with its uniform absolute remainder, but does not establish external novelty. No extra source anchor is needed beyond SOURCES.md.

Falsification checks: the factor \(L\) in (5) and \(L^2\) in \(a_p\) are essential; the sign is negative because \(h'(p)<0\); the baseline is \(y/L\) rather than \(y/\log(p+y)\); the proof keeps the positive logarithmic-weight correction \(S_p\), the selected endpoint \(\Delta(p)\), and the subleading \(h-k\) term. The \(5/6\) exponent is only the cubic Taylor-remainder boundary for this frozen-kernel representation, not a prime-distribution theorem. The Guth–Maynard window is still \(p^{3/4+o(1)}\), so it lies strictly within the absolute-approximation range.

The equivalence (15) concerns the **direct initial integral only** and is not itself a Robin inequality. Prime events inside that interval can still influence the later \(\Delta(t)\) through the remote integral in (16). No theorem here forces a sign or \(o(1)\) bound for \(D_p(H_\star)\), excludes an infinite family of Robin counterexamples, bounds the remaining annular excursion, or proves RH. Its source-specific contribution is an exact, auditable signed moment that replaces the absolute counting-error loss at RE-252's unresolved frontier.