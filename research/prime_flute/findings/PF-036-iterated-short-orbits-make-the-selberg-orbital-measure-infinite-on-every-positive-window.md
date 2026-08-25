# PF-036 — iterated short orbits make the Selberg orbital measure infinite on every positive length window

**Status:** `DECISIVE-NEGATIVE` for recovering distinguished cuff lengths from any standard/global wave-trace or Selberg-trace time localization.

## 1. Input already established for the prime flute

Previous prime-flute findings establish that there are infinitely many distinct primitive closed geodesics

\[
\gamma_j,
\qquad L_j:=\ell(\gamma_j)\to0.
\]

These are the nonlocal separating geodesics produced by isolated multi-gap prime configurations; they are not the distinguished cuffs \(\ell_n\), which instead tend to infinity.

## 2. The complete periodic-orbit length set is dense in \((0,\infty)\)

For any fixed \(t>0\), choose

\[
k_j=\left\lfloor \frac{t}{L_j}+\frac12\right\rfloor.
\]

Then \(k_j\ge1\) for large \(j\) and

\[
|k_jL_j-t|\le \frac{L_j}{2}\to0.
\]

Hence the lengths of repeated closed geodesics

\[
\{k\ell(\gamma):\gamma\ \text{primitive},\ k\ge1\}
\]

are dense in \((0,\infty)\).

This alone implies that no distinguished cuff time \(t=\ell_n\) can be isolated from the complete periodic-orbit length set by a nonempty open time window.

## 3. Stronger statement: the Selberg hyperbolic orbital measure has infinite mass in every positive window

The hyperbolic term in the standard Selberg trace formula uses the weighted atomic measure

\[
\mu_{\rm hyp}
=
\sum_{\gamma\ \mathrm{primitive}}
\sum_{k\ge1}
\frac{\ell_\gamma}{2\sinh(k\ell_\gamma/2)}
\,\delta_{k\ell_\gamma}.
\]

Fix any nonempty compact interval

\[
I=[a,b]\subset(0,\infty),
\qquad a<b.
\]

Choose a smaller interval

\[
J=[a',b']\subset(a,b)
\]

with \(a'<b'\). For every sufficiently large \(j\), let

\[
K_j=\{k\ge1:kL_j\in J\}.
\]

Elementary counting gives

\[
\#K_j
\ge
\frac{b'-a'}{2L_j}
\]

for all large \(j\). For \(k\in K_j\),

\[
2\sinh(kL_j/2)\le 2\sinh(b'/2),
\]

so each weight satisfies

\[
\frac{L_j}{2\sinh(kL_j/2)}
\ge
\frac{L_j}{2\sinh(b'/2)}.
\]

Therefore the total contribution of the iterates of the **single** primitive orbit \(\gamma_j\) inside \(J\) is bounded below uniformly in \(j\):

\[
\sum_{k\in K_j}
\frac{L_j}{2\sinh(kL_j/2)}
\ge
\frac{b'-a'}{4\sinh(b'/2)}=:c_J>0.
\]

Summing over the infinitely many distinct primitive \(\gamma_j\) gives

\[
\boxed{
\mu_{\rm hyp}(J)=\infty.
}
\]

Since \(J\) was an arbitrary positive length window,

\[
\boxed{
\mu_{\rm hyp}(I)=\infty
\quad\text{for every nonempty }I\Subset(0,\infty).
}
\]

Thus the formal hyperbolic orbital measure is not merely non-Radon near length zero: it is **nowhere locally finite on the entire positive length axis**.

Equivalently, if \(g\in C_c^\infty((0,\infty))\) is nonnegative and strictly positive on some interval, then the formal Selberg hyperbolic sum

\[
\sum_{\gamma\ \mathrm{primitive}}
\sum_{k\ge1}
\frac{\ell_\gamma}{2\sinh(k\ell_\gamma/2)}
\,g(k\ell_\gamma)
\]

diverges to \(+\infty\).

## 4. Spectral consequence for the distinguished cuffs

For finite-geometry surfaces, wave/Selberg trace methods recover closed-geodesic lengths by localizing the geometric trace near isolated periodic-orbit times. Here that mechanism fails globally at **every** positive time.

In particular, even though each distinguished cuff length

\[
\ell_n\sim2\log\frac{4p_n}{g_n}
\]

is an intrinsic closed-geodesic length, no compactly supported time window around \(\ell_n\) removes the contribution of the short-orbit sector: infinitely many iterates of the \(L_j\to0\) family lie in every such window, and their Selberg weights have infinite total mass.

Therefore the branch

\[
\boxed{
\ell_n
\to
\text{isolated wave-trace singularity / localized Selberg orbital term}
\to
\text{spectral recovery of prime-gap fluctuations}
}
\]

is decisively ruled out for the **global** prime-flute trace.

This is stronger than the earlier obstruction at time zero: removing a neighborhood of \(0\) does not restore local finiteness.

## 5. Relation to previous findings

- PF-020: primitive lengths accumulate at zero, so the ordinary geometric wave-trace measure already fails to be locally finite near \(0\).
- PF-033: the ordinary heat trace / absolute zeta determinant diverges.
- PF-035: the ordinary Selberg/Ruelle Euler product has no nontrivial initial half-plane of convergence.
- PF-036: **all iterates of the same short primitive family spread this obstruction across every positive time window.**

Thus no standard local-in-time trace regularization can isolate the long distinguished cuffs.

## 6. Novelty / literature check

Known background:

- The standard Selberg hyperbolic weight is
  \(\ell_\gamma/[2\sinh(k\ell_\gamma/2)]\).
- Guillopé-Zworski wave-trace formulas and the usual resonance/length-spectrum theory assume finite geometry.
- Basmajian-Kim and recent Fanoni-Fisac work emphasize that infinite-type surfaces may have non-discrete length spectrum and treat discreteness as a special extra hypothesis.

Directed searches did not locate a trace formula for infinite-type hyperbolic surfaces whose primitive length spectrum accumulates at zero, nor a treatment of the specific consequence above. The statement itself is elementary once \(L_j\to0\) is known, so historical novelty is not claimed. Its role here is a structural obstruction specific to the prime-flute program.

## 7. What remains open

This does **not** rule out spatially localized or relative spectral observables that first isolate a finite geometric subsurface before tracing. PF-034 remains compatible with such localization because it uses pointed geometric tangents and Weyl sequences rather than a global trace.

Any future trace/determinant construction must therefore subtract or reorganize the infinite short-orbit sector **before** time localization. A cutoff only in length/time, or a standard Selberg test function supported away from zero, cannot work.
